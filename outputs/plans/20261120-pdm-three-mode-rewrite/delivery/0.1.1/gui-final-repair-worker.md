# Final GUI and job-lifecycle repair

Status: complete and frozen for parent integration/publication checks. This report records the new scoped repair on 2026-11-20 and supersedes the earlier GUI repair's failed-snapshot retention and redraw coverage claims.

## Failed snapshots and bounded reservations

`raw/code/PDM/GUI/src/multipolepdm/jobs/manager.py` now retains a failed immutable result and summary in a manager-owned cache. Each retained snapshot keeps its existing result-buffer reservation and task-slot reservation. The existing two-result semaphore bounds the combined calculation, disk-write, and retained-failure buffers; the cache cannot grow independently of that bound.

- `open_saved` also opens retained failed snapshots, returning `data_state="save_failed"` and the saved error text. `gui/window.py` preserves that display state so Open selected result restores Retry data save after preview eviction.
- Retry uses the manager's authoritative snapshot and transfers the existing reservations to the new write. It does not acquire another result buffer or task slot. This permits retry even when later queued jobs have filled the submission queue and are waiting for result capacity.
- Repeated disk failures keep the same reservations. A failed retry submission restores the original job and directory without discarding the snapshot or releasing its reservations.
- Cancelling a retained failed task discards its buffer and releases both reservations. Cancelling a calculation waiting for result capacity is checked during bounded semaphore waits, so it can terminate while other failed tasks still occupy both buffers.
- Shutdown releases retained failures before joining the calculator. Failures occurring during shutdown do not retain new buffers. Graceful shutdown can therefore drain queued jobs, while cancellation shutdown also cancels waiting work. Reservation-balance tests verify that every semaphore permit is returned.

Two retained failures deliberately pause further calculation until a failure is retried, cancelled, or the manager closes. This is bounded backpressure. Saved results remain reopenable from disk; retained failed results are recoverable during the manager lifetime, not persisted across application shutdown.

The preview cache remains capped at three pending previews and three displayed windows. Eviction no longer destroys the sole recoverable copy of a failed save. Retry uses a newly reserved output directory; the original failed output and raw input snapshots are not overwritten.

## Nonblocking canvas redraws

`raw/code/PDM/GUI/src/multipolepdm/gui/results.py` adds `DeferredFigureCanvas`, used for result previews. Its `draw()` attempts `MATPLOTLIB_LOCK` without blocking. When busy, it coalesces requests into one single-shot Qt child timer, retrying after 50 ms. When available, the lock covers the synchronous superclass draw, preventing a worker export from entering its render section concurrently.

This applies to direct drawing, inherited idle drawing, Restore full ranges, toolbar navigation, and resize-triggered drawing. Closing a result window or canvas stops the retry timer and suppresses subsequent draw requests. Background figure saving and frozen computed results retain their existing behavior.

## Actual verification

Commands ran from `raw/code/PDM/GUI` with `PYTHONPATH=src` and `QT_QPA_PLATFORM=offscreen`.

Before the repair, three new regressions failed in 16.86 seconds:

- Reopening a failed snapshot raised `This task has no saved result to open`.
- Drawing during a real PDF export, with the worker holding `Figure._render_lock` inside the export's `savefig`, produced a **5.458616 s** GUI heartbeat gap.
- A failed preview evicted by four subsequent successful jobs could not be recovered through Open selected result.

Evidence: `tmp/pdm-upgrade-011/gui-final-red.log`.

The focused repaired run passed 10 tests in 9.76 seconds. Evidence: `tmp/pdm-upgrade-011/gui-final-targeted.log` and `gui-final-targeted.xml`.

The final regression command exited 0 with **34 passed in 43.79 seconds**:

```bash
PYTHONPATH=src QT_QPA_PLATFORM=offscreen pytest -q \
  tests/test_jobs.py tests/test_app_regressions.py \
  tests/test_gui.py tests/test_gui_averaging.py \
  -o junit_family=legacy \
  --junitxml=/workspace/wiki/tmp/pdm-upgrade-011/gui-final-regression.xml
```

Evidence: `tmp/pdm-upgrade-011/gui-final-regression.log` and `gui-final-regression.xml`.

Measured maximum heartbeat gaps in that final run:

| Scenario | Maximum gap |
|---|---:|
| Second result ready during a blocked figure export | 0.0180304 s |
| Restore, toolbar, resize, repeated direct/idle draws during held export render | 0.0105844 s |
| Same redraw contention followed by closing the pending canvas | 0.0105163 s |

The redraw tests verify one child retry timer, no premature render while the export holds the lock, eventual restored axis limits and valid PDF output, and no late rendering after close. The failed-preview test runs a real initial successful job, a failed job, and four later successes under the export lock; it reopens the evicted failure, retries to a healthy directory, verifies frozen-array identity and saved density values, and confirms exactly one calculation of that failed job.

Job tests additionally cover full-queue retry with two retained failures, cancellation while waiting for capacity, graceful and cancelling shutdown with blocked jobs, retry-submission rollback, repeated failed retries, cancellation during a failing write, and balanced result/task permits. Existing slow-disk, save-manifest, export, batch reopen, input, and azimuth regressions also pass.

Ruff passed on the five changed Python files using `--ignore BLE001`, preserving the existing broad exception handlers at GUI/worker error boundaries. Evidence: `tmp/pdm-upgrade-011/gui-final-lint.log`. Regression warnings are the existing Qt backend deprecation warnings. No full-production-suite or wheel rebuild is claimed by this worker; the parent can resume those checks on the frozen files.

## Changed files

- `raw/code/PDM/GUI/src/multipolepdm/gui/window.py`
- `raw/code/PDM/GUI/src/multipolepdm/gui/results.py`
- `raw/code/PDM/GUI/src/multipolepdm/jobs/manager.py`
- `raw/code/PDM/GUI/tests/test_app_regressions.py`
- `raw/code/PDM/GUI/tests/test_jobs.py`

No physics, statistics, worker-computation, plotting/export, original snapshot, or documentation files were changed. No Git operations or child agents were used.
