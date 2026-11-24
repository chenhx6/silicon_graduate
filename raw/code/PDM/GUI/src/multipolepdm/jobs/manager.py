"""Bounded calculation and disk queues; ready always precedes save completion."""

import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field, fields, is_dataclass, replace
from queue import Queue
from threading import BoundedSemaphore, Event, Lock

import numpy as np

from multipolepdm.io.export import (
    export_result,
    load_snapshot,
    reserve_result_directory,
)
from multipolepdm.jobs.workers import Cancelled, compute_job


@dataclass
class TaskHandle:
    job_id: str
    job: object
    directory: object
    cancellation: Event = field(default_factory=Event)
    state: str = "queued"


class QueueFull(RuntimeError):
    pass


def freeze_arrays(value):
    """Consumers can plot shared snapshots but cannot edit an in-flight export."""
    if isinstance(value, np.ndarray):
        value.setflags(write=False)
    elif is_dataclass(value):
        for item in fields(value):
            freeze_arrays(getattr(value, item.name))
    elif isinstance(value, (tuple, list)):
        for item in value:
            freeze_arrays(item)


class JobManager:
    def __init__(self, compute=compute_job, writer=export_result, max_pending=8):
        self.events = Queue()
        self.handles = {}
        self._lock = Lock()
        self._slots = BoundedSemaphore(max_pending)
        self._results = BoundedSemaphore(2)
        self._failed = {}
        self._compute = compute
        self._writer = writer
        self._calculator = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="pdm-calculate"
        )
        self._disk = ThreadPoolExecutor(max_workers=1, thread_name_prefix="pdm-save")
        self._closed = False

    def _notify(self, handle, state, **payload):
        self.events.put(
            {
                "job_id": handle.job_id,
                "state": state,
                "directory": str(handle.directory),
                **payload,
            }
        )

    def _event(self, handle, state, **payload):
        handle.state = state
        self._notify(handle, state, **payload)

    def _acquire_slot(self):
        if self._closed:
            raise RuntimeError("Job manager is closed.")
        if not self._slots.acquire(blocking=False):
            raise QueueFull("Queue is full. Wait for a task to finish or cancel one.")

    def submit(self, job):
        with self._lock:
            self._acquire_slot()
            try:
                handle = TaskHandle(uuid.uuid4().hex, job, reserve_result_directory(job))
                self.handles[handle.job_id] = handle
                self._event(handle, "queued")
                self._calculator.submit(self._run, handle)
                return handle.job_id
            except Exception:
                self._slots.release()
                raise

    def retry_save(self, job_id, result, summary, destination):
        with self._lock:
            handle = self.handles[job_id]
            if self._closed:
                raise RuntimeError("Job manager is closed.")
            if handle.state != "save_failed" or job_id not in self._failed:
                raise RuntimeError("Only a failed data save can be retried.")
            result, summary, _ = self._failed[job_id]
            output = replace(handle.job.output, directory=destination)
            job = replace(handle.job, output=output)
            directory = reserve_result_directory(job)
            snapshot = replace(result, job=job)
            previous_job, previous_directory = handle.job, handle.directory
            try:
                handle.job, handle.directory = job, directory
                handle.cancellation.clear()
                self._event(handle, "queued")
                self._disk.submit(self._save, handle, snapshot, summary)
                self._failed.pop(job_id)
            except Exception as exc:
                handle.job, handle.directory = previous_job, previous_directory
                self._event(handle, "save_failed", error=str(exc))
                raise

    def open_saved(self, job_id):
        """Open a saved result or the bounded retained snapshot of a failed save."""
        with self._lock:
            handle = self.handles[job_id]
            if self._closed:
                raise RuntimeError("Job manager is closed.")
            if handle.state == "save_failed" and job_id in self._failed:
                result, summary, error = self._failed[job_id]
                self._notify(
                    handle, "opened", result=result, summary=summary,
                    data_state="save_failed", error=error,
                )
                return
            if handle.state != "saved":
                raise RuntimeError("This task has no saved result to open.")
            self._disk.submit(self._open, handle)

    def _open(self, handle):
        try:
            result, summary = load_snapshot(handle.directory)
            freeze_arrays(result)
            freeze_arrays(summary)
            self._notify(handle, "opened", result=result, summary=summary)
        except Exception as exc:
            self._notify(handle, "open_failed", error=str(exc))

    def cancel(self, job_id):
        with self._lock:
            handle = self.handles[job_id]
            handle.cancellation.set()
            if job_id in self._failed:
                self._failed.pop(job_id)
                self._event(handle, "cancelled")
                self._results.release()
                self._slots.release()

    def _run(self, handle):
        acquired = False
        try:
            while not acquired:
                if handle.cancellation.is_set():
                    raise Cancelled("Cancelled while waiting for result capacity.")
                acquired = self._results.acquire(timeout=0.05)
            if handle.cancellation.is_set():
                raise Cancelled("Cancelled before computation.")
            self._event(handle, "calculating", percent=0)
            result, summary = self._compute(
                handle.job,
                handle.cancellation.is_set,
                lambda p: self._event(handle, "calculating", percent=p),
            )
            freeze_arrays(result)
            freeze_arrays(summary)
            self._event(handle, "ready", result=result, summary=summary, percent=100)
            self._disk.submit(self._save, handle, result, summary)
        except Exception as exc:
            self._event(
                handle,
                "cancelled" if isinstance(exc, Cancelled) else "calculation_failed",
                error=str(exc),
            )
            if acquired:
                self._results.release()
            self._slots.release()

    def _save(self, handle, result, summary):
        retained = False
        try:
            handle.directory = handle.directory.expanduser()
            self._event(handle, "saving", percent=0)
            handle.directory.mkdir(parents=True, exist_ok=False)
            outcome = self._writer(
                result,
                summary,
                handle.directory,
                handle.cancellation.is_set,
                lambda p: self._event(handle, "saving", percent=p),
            )
            if outcome not in ("saved", "cancelled"):
                raise ValueError("Data writer must return 'saved' or 'cancelled'.")
            self._event(handle, outcome, percent=100)
        except Exception as exc:
            with self._lock:
                if handle.cancellation.is_set():
                    self._event(handle, "cancelled", error=str(exc))
                else:
                    if not self._closed:
                        self._failed[handle.job_id] = (result, summary, str(exc))
                        retained = True
                    self._event(handle, "save_failed", error=str(exc))
        finally:
            if not retained:
                self._results.release()
                self._slots.release()

    def shutdown(self, wait=True, cancel=False):
        with self._lock:
            self._closed = True
            if cancel:
                for handle in self.handles.values():
                    handle.cancellation.set()
            for _ in self._failed:
                self._results.release()
                self._slots.release()
            self._failed.clear()
        # Calculator must finish enqueueing its writes before disk shutdown.
        self._calculator.shutdown(wait=True)
        self._disk.shutdown(wait=wait)
