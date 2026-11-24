import time
from dataclasses import dataclass, replace
from threading import Event, Thread

import numpy as np
import pytest

from multipolepdm.contracts import OutputSpec
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.jobs.manager import JobManager


def wait_event(manager, state, seconds=5, job_id=None):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        event = manager.events.get(timeout=seconds)
        if event["state"] == state and (job_id is None or event["job_id"] == job_id):
            return event
    raise AssertionError(state)


def test_ready_before_slow_disk_and_next_compute(tmp_path):
    entered, release = Event(), Event()
    count = []

    def compute(job, cancelled, progress):
        count.append(job.label)
        return object(), object()

    def writer(*args):
        entered.set()
        assert release.wait(5)

    manager = JobManager(compute=compute, writer=writer)
    job = replace(job_from_dict(example_data()), output=OutputSpec(str(tmp_path)))
    try:
        first = manager.submit(job)
        assert wait_event(manager, "ready")["job_id"] == first
        assert entered.wait(3)
        second = manager.submit(replace(job, label="second"))
        assert wait_event(manager, "ready")["job_id"] == second
        assert count == [job.label, "second"]
        assert manager.handles[first].directory != manager.handles[second].directory
    finally:
        release.set()
        manager.shutdown()


def test_disk_failure_does_not_remove_preview(tmp_path):
    def writer(*args):
        raise OSError("Disk full")

    manager = JobManager(compute=lambda *args: ("result", "summary"), writer=writer)
    job = replace(job_from_dict(example_data()), output=OutputSpec(str(tmp_path)))
    try:
        manager.submit(job)
        assert wait_event(manager, "ready")["result"] == "result"
        assert "Disk full" in wait_event(manager, "save_failed")["error"]
    finally:
        manager.shutdown()


def test_bounded_queue(tmp_path):
    release = Event()

    def compute(*args):
        release.wait(3)
        return None, None

    manager = JobManager(compute=compute, writer=lambda *args: None, max_pending=1)
    job = replace(job_from_dict(example_data()), output=OutputSpec(str(tmp_path)))
    try:
        manager.submit(job)
        with pytest.raises(RuntimeError, match="Queue is full"):
            manager.submit(job)
    finally:
        release.set()
        manager.shutdown()


@dataclass
class Snapshot:
    job: object
    values: np.ndarray


def failing_manager(tmp_path, max_pending=3):
    computations = []
    writes = []

    def compute(job, cancelled, progress):
        computations.append(job.label)
        return Snapshot(job, np.ones(3)), np.ones(2)

    def writer(result, summary, directory, *args):
        writes.append((result, summary))
        if directory.parent.name != "healthy":
            raise OSError("Disk full")
        return "saved"

    manager = JobManager(compute=compute, writer=writer, max_pending=max_pending)
    job = replace(job_from_dict(example_data()), output=OutputSpec(str(tmp_path)))
    return manager, job, computations, writes


def assert_reservations_released(manager, slots):
    for semaphore, count in ((manager._results, 2), (manager._slots, slots)):
        for _ in range(count):
            assert semaphore.acquire(blocking=False)
        assert not semaphore.acquire(blocking=False)
        for _ in range(count):
            semaphore.release()


def test_failed_snapshots_reopen_and_retry_with_full_queue(tmp_path):
    manager, job, computations, writes = failing_manager(tmp_path)
    try:
        first = manager.submit(replace(job, label="first"))
        wait_event(manager, "save_failed", job_id=first)
        second = manager.submit(replace(job, label="second"))
        wait_event(manager, "save_failed", job_id=second)
        third = manager.submit(replace(job, label="third"))
        manager.open_saved(first)
        opened = wait_event(manager, "opened", job_id=first)
        assert opened["data_state"] == "save_failed"
        assert opened["result"] is writes[0][0]
        assert not opened["result"].values.flags.writeable
        assert not opened["summary"].flags.writeable
        assert computations == ["first", "second"]
        with pytest.raises(RuntimeError, match="Queue is full"):
            manager.submit(job)
        manager.retry_save(first, opened["result"], opened["summary"], str(tmp_path / "healthy"))
        wait_event(manager, "saved", job_id=first)
        wait_event(manager, "save_failed", job_id=third)
        assert computations == ["first", "second", "third"]
        assert writes[2][0].values is writes[0][0].values
        assert writes[2][1] is writes[0][1]
        manager.cancel(second)
        manager.cancel(third)
        assert manager.handles[second].state == manager.handles[third].state == "cancelled"
    finally:
        manager.shutdown(cancel=True)
    assert_reservations_released(manager, 3)


def test_cancel_task_waiting_for_failed_snapshot_capacity(tmp_path):
    manager, job, computations, _ = failing_manager(tmp_path)
    try:
        first = manager.submit(replace(job, label="first"))
        wait_event(manager, "save_failed")
        second = manager.submit(replace(job, label="second"))
        wait_event(manager, "save_failed")
        third = manager.submit(replace(job, label="waiting"))
        manager.cancel(third)
        wait_event(manager, "cancelled", job_id=third)
        assert computations == ["first", "second"]
        manager.cancel(first)
        manager.cancel(second)
    finally:
        manager.shutdown(cancel=True)
    assert_reservations_released(manager, 3)


@pytest.mark.parametrize("cancel", [False, True])
def test_shutdown_releases_failed_buffers_and_drains_waiting_jobs(tmp_path, cancel):
    manager, job, _, _ = failing_manager(tmp_path, max_pending=5)
    manager.submit(job)
    wait_event(manager, "save_failed")
    manager.submit(job)
    wait_event(manager, "save_failed")
    for _ in range(3):
        manager.submit(job)
    errors = []

    def shutdown():
        try:
            manager.shutdown(cancel=cancel)
        except Exception as exc:
            errors.append(exc)

    closer = Thread(target=shutdown, daemon=True)
    closer.start()
    closer.join(5)
    assert not closer.is_alive(), "Shutdown is blocked behind retained failed snapshots"
    assert not errors
    assert_reservations_released(manager, 5)


def test_retry_submission_failure_keeps_original_snapshot_and_reservations(tmp_path, monkeypatch):
    manager, job, computations, writes = failing_manager(tmp_path, max_pending=1)
    try:
        identifier = manager.submit(job)
        wait_event(manager, "save_failed")
        original_directory = manager.handles[identifier].directory
        submit = manager._disk.submit

        def reject(*args, **kwargs):
            raise RuntimeError("Injected submission failure")

        monkeypatch.setattr(manager._disk, "submit", reject)
        with pytest.raises(RuntimeError, match="Injected"):
            manager.retry_save(identifier, *writes[0], str(tmp_path / "healthy"))
        assert manager.handles[identifier].directory == original_directory
        assert manager.handles[identifier].state == "save_failed"
        monkeypatch.setattr(manager._disk, "submit", submit)
        manager.open_saved(identifier)
        assert wait_event(manager, "opened")["result"] is writes[0][0]
        manager.retry_save(identifier, *writes[0], str(tmp_path / "healthy"))
        wait_event(manager, "saved")
        assert len(computations) == 1
    finally:
        manager.shutdown(cancel=True)
    assert_reservations_released(manager, 1)


def test_repeated_failed_retries_reuse_one_reservation(tmp_path):
    manager, job, computations, writes = failing_manager(tmp_path, max_pending=1)
    try:
        identifier = manager.submit(job)
        wait_event(manager, "save_failed")
        for index in range(3):
            manager.retry_save(identifier, *writes[0], str(tmp_path / f"bad-{index}"))
            wait_event(manager, "save_failed", job_id=identifier)
            assert len(manager._failed) == 1
            with pytest.raises(RuntimeError, match="Queue is full"):
                manager.submit(job)
        manager.retry_save(identifier, *writes[0], str(tmp_path / "healthy"))
        wait_event(manager, "saved")
        assert len(computations) == 1
        assert all(result.values is writes[0][0].values for result, summary in writes)
    finally:
        manager.shutdown(cancel=True)
    assert_reservations_released(manager, 1)


def test_cancel_during_failing_write_discards_snapshot_and_releases_capacity(tmp_path):
    entered, release = Event(), Event()

    def writer(*args):
        entered.set()
        assert release.wait(5)
        raise OSError("Failure after cancellation")

    manager = JobManager(compute=lambda *args: (None, None), writer=writer, max_pending=1)
    job = replace(job_from_dict(example_data()), output=OutputSpec(str(tmp_path)))
    try:
        identifier = manager.submit(job)
        assert entered.wait(5)
        manager.cancel(identifier)
        release.set()
        wait_event(manager, "cancelled", job_id=identifier)
        assert not manager._failed
    finally:
        release.set()
        manager.shutdown(cancel=True)
    assert_reservations_released(manager, 1)
