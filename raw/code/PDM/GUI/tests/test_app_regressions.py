import json
from dataclasses import replace
from pathlib import Path
from threading import Event, Thread, get_ident
from time import monotonic

import numpy as np
import pytest
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QFileDialog

from multipolepdm.gui.window import MainWindow
from multipolepdm.io import export
from multipolepdm.io.input import example_data, job_from_dict
from multipolepdm.jobs import manager as jobs
from multipolepdm.jobs.workers import compute_job


def small_example(mode="P_ADO"):
    data = example_data(mode)
    data["grid"].update(xi_points=101, sigma_points=41, xi_step_rad=None, sigma_step=None)
    return data


@pytest.fixture
def make_window(qtbot):
    windows = []

    def create(destination, manager=None):
        window = MainWindow(manager=manager)
        qtbot.addWidget(window)
        windows.append(window)
        window.output_path.setText(str(destination))
        window.grid_editor.recommended.setChecked(False)
        window.grid_editor.values["angle_step"].setValue(1.0)
        window.grid_editor.values["width_step"].setValue(0.025)
        window.show()
        return window

    yield create
    for window in windows:
        window.manager.shutdown(cancel=True)
        window.process_events()
        window.close()


def wait_for_row(qtbot, window, index, state):
    qtbot.waitUntil(
        lambda: window.task_list.count() > index
        and window.task_list.itemText(index).endswith(f" | {state}"),
        timeout=15000,
    )
    return window.task_list.itemData(index)


def start_heartbeat(window):
    ticks = []
    timer = QTimer(window)
    timer.timeout.connect(lambda: ticks.append(get_ident()))
    timer.start(10)
    return ticks


def test_invalid_output_keeps_visible_save_failure_and_preview(
    qtbot, tmp_path, make_window
):
    destination = tmp_path / "regular-file"
    destination.write_text("existing content", encoding="utf-8")
    window = make_window(destination)
    window.calculate_button.click()

    identifier = wait_for_row(qtbot, window, 0, "save_failed")
    preview = window.result_windows[identifier]
    assert preview.isVisible() and preview.retry_button.isVisible()
    assert str(destination) in preview.status.text()
    assert str(destination) in window.status.text()
    assert window.manager.handles[identifier].state == "save_failed"
    assert destination.read_text(encoding="utf-8") == "existing content"


def test_slow_mkdir_leaves_gui_responsive_and_inputs_editable(
    qtbot, tmp_path, make_window, monkeypatch
):
    destination = tmp_path / "slow"
    window = make_window(destination)
    window.label.setText("Frozen before mkdir")
    ticks = start_heartbeat(window)
    mkdir_started = Event()
    release = Event()
    worker_threads = []
    real_mkdir = Path.mkdir

    def slow_mkdir(path, *args, **kwargs):
        if path.parent == destination and not kwargs.get("exist_ok"):
            worker_threads.append(get_ident())
            mkdir_started.set()
            assert release.wait(5), "mkdir blocked the GUI thread"
        return real_mkdir(path, *args, **kwargs)

    monkeypatch.setattr(Path, "mkdir", slow_mkdir)
    try:
        window.calculate_button.click()
        qtbot.waitUntil(mkdir_started.is_set, timeout=10000)
        before = len(ticks)
        qtbot.waitUntil(lambda: len(ticks) > before, timeout=2000)
        assert worker_threads and all(thread != get_ident() for thread in worker_threads)
        assert window.label.isEnabled()
        window.label.setText("Next calculation")
    finally:
        release.set()
    identifier = wait_for_row(qtbot, window, 0, "saved")
    result = export.load_result(window.manager.handles[identifier].directory)
    assert result.job.label == "Frozen before mkdir"


def test_enospc_retry_uses_preview_without_recomputing(
    qtbot, tmp_path, make_window, monkeypatch
):
    computations = []
    snapshots = []

    def compute(job, cancelled, progress):
        computations.append(job)
        return compute_job(job, cancelled, progress)

    def writer(result, summary, directory, cancelled, progress):
        snapshots.append((result.parameter_density, summary))
        return export.export_result(result, summary, directory, cancelled, progress)

    manager = jobs.JobManager(compute=compute, writer=writer)
    window = make_window(tmp_path / "original", manager)
    npz_writer = export.np.savez_compressed

    def raise_enospc(*args, **kwargs):
        raise OSError(28, "No space left on device")

    monkeypatch.setattr(export.np, "savez_compressed", raise_enospc)
    window.calculate_button.click()
    identifier = wait_for_row(qtbot, window, 0, "save_failed")
    preview = window.result_windows[identifier]
    previous = manager.handles[identifier].directory
    assert preview.retry_button.isVisible()
    assert "No space left on device" in preview.status.text()

    monkeypatch.setattr(export.np, "savez_compressed", npz_writer)
    destination = tmp_path / "retry-destination"
    destination.mkdir()
    monkeypatch.setattr(QFileDialog, "getExistingDirectory", lambda *args: str(destination))
    window.label.setText("Different later input")
    window.fields["target_initial"].setValue(91)
    preview.retry_button.click()

    assert wait_for_row(qtbot, window, 0, "saved") == identifier
    assert window.task_list.count() == 1 and len(computations) == 1
    assert len(snapshots) == 2
    assert snapshots[0][0] is snapshots[1][0] is preview.result.parameter_density
    assert snapshots[0][1] is snapshots[1][1] is preview.summary
    assert window.result_windows[identifier] is preview and not preview.retry_button.isVisible()
    actual = manager.handles[identifier].directory
    assert actual.parent == destination
    assert preview.directory == actual
    assert json.loads((previous / "manifest.json").read_text())["status"] == "save_failed"
    result = export.load_result(actual)
    assert result.job == replace(computations[0], output=replace(computations[0].output, directory=str(destination)))


def test_nine_file_jobs_reopen_first_snapshot_off_thread(
    qtbot, tmp_path, make_window, monkeypatch
):
    data = [small_example(mode) for mode in ("P_ADO", "P_DCO", "PDCO") * 3]
    for index, entry in enumerate(data):
        entry["label"] = f"batch-{index}"
    source = tmp_path / "jobs.json"
    source.write_text(json.dumps({"jobs": data}), encoding="utf-8")
    window = make_window(tmp_path / "results")
    window.file_path.setText(str(source))
    window.file_mode.setChecked(True)
    window.mode.setCurrentText("PDCO")
    window.fields["target_initial"].setValue(91)
    window.calculate_button.click()
    assert len(window.pending_jobs) >= 1
    qtbot.waitUntil(
        lambda: window.task_list.count() == 9
        and all(window.task_list.itemText(index).endswith(" | saved") for index in range(9)),
        timeout=45000,
    )
    identifiers = [window.task_list.itemData(index) for index in range(9)]
    handles = [window.manager.handles[identifier] for identifier in identifiers]
    assert len({handle.directory for handle in handles}) == 9
    for handle, expected in zip(handles, data):
        requested = job_from_dict(expected)
        assert replace(export.load_result(handle.directory).job, output=requested.output) == requested
    first = identifiers[0]
    assert first not in window.result_windows
    assert len(window.result_windows) <= 3

    load_started = Event()
    release = Event()
    loaded = []
    ticks = start_heartbeat(window)

    def held_load(directory):
        loaded.append((directory, get_ident()))
        load_started.set()
        assert release.wait(5), "loading blocked the GUI thread"
        return export.load_snapshot(directory)

    monkeypatch.setattr(jobs, "load_snapshot", held_load)
    window.task_list.setCurrentIndex(0)
    try:
        window.open_button.click()
        qtbot.waitUntil(load_started.is_set, timeout=5000)
        assert not window.open_button.isEnabled()
        before = len(ticks)
        qtbot.waitUntil(lambda: len(ticks) > before, timeout=2000)
        assert loaded == [(handles[0].directory, loaded[0][1])]
        assert loaded[0][1] != get_ident()
    finally:
        release.set()
    qtbot.waitUntil(lambda: first in window.result_windows, timeout=10000)
    preview = window.result_windows[first]
    assert preview.result.job == handles[0].job
    assert len(window.result_windows) <= 3 and window.open_button.isEnabled()
    assert "save_figure" not in {item[3] for item in preview.toolbar.toolitems}
    saved_summary = json.loads((handles[0].directory / "summary.json").read_text())
    np.testing.assert_array_equal(preview.summary.delta_pdf.density, saved_summary["delta_pdf"]["density"])
    assert not preview.result.parameter_density.flags.writeable
    assert not preview.summary.delta.density.flags.writeable
    preview.close()
    assert first not in window.result_windows
    window.open_button.click()
    qtbot.waitUntil(lambda: first in window.result_windows, timeout=10000)
    assert window.result_windows[first] is not preview


@pytest.mark.parametrize(
    ("cancel_percent", "full_csv", "expected"),
    [(100, False, "saved"), (100, True, "saved"), (25, False, "cancelled")],
)
def test_save_terminal_event_follows_committed_manifest(
    tmp_path, cancel_percent, full_csv, expected
):
    job = job_from_dict(small_example())
    job = replace(job, output=replace(job.output, directory=str(tmp_path), full_csv=full_csv))
    committed_on_cancel = []
    submitted = Event()

    def writer(result, summary, directory, cancelled, progress):
        def cancel_during_progress(percent):
            progress(percent)
            if percent == cancel_percent:
                committed_on_cancel.append(json.loads((directory / "manifest.json").read_text())["status"])
                assert submitted.wait(5)
                manager.cancel(identifier)

        return export.export_result(result, summary, directory, cancelled, cancel_during_progress)

    manager = jobs.JobManager(writer=writer)
    try:
        identifier = manager.submit(job)
        submitted.set()
        manager.shutdown()
        handle = manager.handles[identifier]
        manifest = json.loads((handle.directory / "manifest.json").read_text())
        states = []
        while not manager.events.empty():
            states.append(manager.events.get_nowait()["state"])
        assert states[-1] == handle.state == manifest["status"] == expected
        assert len(committed_on_cancel) == 1
        if expected == "saved":
            assert committed_on_cancel == ["saved"]
            assert export.load_result(handle.directory).job == job
    finally:
        manager.shutdown(cancel=True)


def test_writer_without_a_terminal_outcome_does_not_report_saved(tmp_path):
    job = job_from_dict(small_example())
    job = replace(job, output=replace(job.output, directory=str(tmp_path)))
    manager = jobs.JobManager(
        compute=lambda *args: (None, None),
        writer=lambda *args: None,
    )
    try:
        identifier = manager.submit(job)
        manager.shutdown()
        assert manager.handles[identifier].state == "save_failed"
        events = []
        while not manager.events.empty():
            events.append(manager.events.get_nowait())
        assert events[-1]["state"] == "save_failed"
        assert "must return 'saved' or 'cancelled'" in events[-1]["error"]
    finally:
        manager.shutdown(cancel=True)


def test_slow_figure_export_defers_second_ready_preview_without_blocking_qt(
    qtbot, tmp_path, make_window, monkeypatch, record_property
):
    from matplotlib.figure import Figure

    window = make_window(tmp_path / "results")
    window.calculate_button.click()
    first = wait_for_row(qtbot, window, 0, "saved")
    qtbot.waitUntil(lambda: first in window.result_windows, timeout=10000)
    original = window.result_windows[first]
    original_density = original.result.parameter_density.copy()
    entered = Event()
    release = Event()
    worker_threads = []
    real_savefig = Figure.savefig
    target = tmp_path / "slow-panel.pdf"

    def slow_savefig(figure, *args, **kwargs):
        worker_threads.append(get_ident())
        entered.set()
        release.wait(4)
        return real_savefig(figure, *args, **kwargs)

    monkeypatch.setattr(Figure, "savefig", slow_savefig)
    monkeypatch.setattr(QFileDialog, "getSaveFileName", lambda *args: (str(target), ""))
    ticks = []
    heartbeat = QTimer(window)
    heartbeat.timeout.connect(lambda: ticks.append(monotonic()))
    heartbeat.start(10)
    try:
        original.save_plot(1)
        qtbot.waitUntil(entered.is_set, timeout=10000)
        ticks.clear()
        ticks.append(monotonic())
        window.label.setText("Second frozen result")
        window.calculate_button.click()
        second = wait_for_row(qtbot, window, 1, "saved")
        qtbot.waitUntil(lambda: len(ticks) >= 10, timeout=5000)
        maximum_gap = float(max(np.diff(ticks)))
        record_property("heartbeat_max_gap_seconds", maximum_gap)
        assert maximum_gap < 0.5
        assert second not in window.result_windows
        assert second in window.pending_previews
        assert len(worker_threads) == 1
        assert worker_threads[0] != get_ident()
        window.label.setText("Later editable input")
        assert window.calculate_button.isEnabled()
        np.testing.assert_array_equal(original.result.parameter_density, original_density)
        assert not original.result.parameter_density.flags.writeable
    finally:
        release.set()
        heartbeat.stop()
    qtbot.waitUntil(lambda: target.exists(), timeout=15000)
    qtbot.waitUntil(lambda: second in window.result_windows, timeout=15000)
    deferred = window.result_windows[second]
    assert deferred.result.job.label == "Second frozen result"
    assert deferred.status.text().startswith("saved:")
    assert not window.pending_previews
    assert target.stat().st_size > 1000
    deferred.close()
    window.task_list.setCurrentIndex(1)
    window.open_button.click()
    qtbot.waitUntil(lambda: second in window.result_windows, timeout=15000)
    assert window.result_windows[second].result.job.label == "Second frozen result"


@pytest.mark.parametrize("close_pending", [False, True])
def test_deferred_previews_are_bounded_and_keep_terminal_state(
    qtbot, tmp_path, make_window, close_pending
):
    from multipolepdm.plotting.style import MATPLOTLIB_LOCK

    window = make_window(tmp_path / "results")
    window.calculate_button.click()
    first = wait_for_row(qtbot, window, 0, "saved")
    qtbot.waitUntil(lambda: first in window.result_windows, timeout=10000)
    original = window.result_windows[first]
    entered, release = Event(), Event()

    def hold_plot_lock():
        with MATPLOTLIB_LOCK:
            entered.set()
            release.wait(10)

    holder = Thread(target=hold_plot_lock)
    holder.start()
    identifiers = []
    try:
        qtbot.waitUntil(entered.is_set, timeout=2000)
        for index in range(5):
            identifier = f"deferred-{index}"
            identifiers.append(identifier)
            window.manager.handles[identifier] = jobs.TaskHandle(
                identifier, original.result.job, original.directory, state="saved"
            )
            window.show_result(identifier, {
                "job_id": identifier, "state": "ready",
                "result": original.result, "summary": original.summary,
                "directory": str(original.directory),
            })
            assert len(window.pending_previews) <= window.MAX_PENDING_PREVIEWS
        assert list(window.pending_previews) == identifiers[-3:]
        for identifier, state in zip(identifiers[-3:], ("save_failed", "cancelled", "saved")):
            window.manager.handles[identifier].state = state
            window.manager.events.put({
                "job_id": identifier, "state": state,
                "directory": str(original.directory), "error": "retained status",
            })
        window.process_events()
        assert not any(identifier in window.result_windows for identifier in identifiers)
        for payload in window.pending_previews.values():
            assert payload["result"] is original.result
            assert payload["summary"] is original.summary
        if close_pending:
            window.close()
            assert not window.pending_previews
            assert not window.timer.isActive()
    finally:
        release.set()
        holder.join(timeout=5)
    if close_pending:
        qtbot.wait(100)
        assert not window.result_windows
    else:
        qtbot.waitUntil(lambda: not window.pending_previews, timeout=15000)
        for identifier, state in zip(identifiers[-3:], ("save_failed", "cancelled", "saved")):
            preview = window.result_windows[identifier]
            assert preview.status.text().startswith(state + ":")
            assert "retained status" in preview.status.text()
            assert preview.retry_button.isVisible() == (state == "save_failed")


@pytest.mark.parametrize("close_pending", [False, True])
def test_restore_resize_and_toolbar_draws_defer_during_export_render(
    qtbot, tmp_path, make_window, monkeypatch, record_property, close_pending
):
    from matplotlib.figure import Figure

    window = make_window(tmp_path / "results")
    window.calculate_button.click()
    identifier = wait_for_row(qtbot, window, 0, "saved")
    qtbot.waitUntil(lambda: identifier in window.result_windows, timeout=10000)
    preview = window.result_windows[identifier]
    preview.preview.axes[0].set_xlim(0, 0.1)
    preview.canvas.draw()
    gui_thread = get_ident()
    entered, release, saving = Event(), Event(), Event()
    real_savefig, real_draw = Figure.savefig, Figure.draw
    rendered = []
    preview.canvas.mpl_connect("draw_event", lambda event: rendered.append(monotonic()))

    def saving_figure(figure, *args, **kwargs):
        saving.set()
        try:
            return real_savefig(figure, *args, **kwargs)
        finally:
            saving.clear()

    def held_render(figure, *args, **kwargs):
        if get_ident() != gui_thread and saving.is_set() and not entered.is_set():
            with Figure._render_lock:
                entered.set()
                release.wait(4)
                return real_draw(figure, *args, **kwargs)
        return real_draw(figure, *args, **kwargs)

    monkeypatch.setattr(Figure, "savefig", saving_figure)
    monkeypatch.setattr(Figure, "draw", held_render)
    target = tmp_path / "held-render.pdf"
    monkeypatch.setattr(QFileDialog, "getSaveFileName", lambda *args: (str(target), ""))
    ticks = []
    heartbeat = QTimer(window)
    heartbeat.timeout.connect(lambda: ticks.append(monotonic()))
    heartbeat.start(10)
    try:
        preview.save_plot(1)
        qtbot.waitUntil(entered.is_set, timeout=10000)
        before = len(rendered)
        ticks[:] = [monotonic()]
        preview.toolbar.home()
        preview.restore_full_ranges()
        preview.canvas.resize(preview.canvas.width() + 50, preview.canvas.height() + 30)
        for _ in range(10):
            preview.canvas.draw_idle()
            preview.canvas.draw()
        ticks.append(monotonic())
        qtbot.waitUntil(lambda: len(ticks) >= 12, timeout=5000)
        maximum_gap = float(max(np.diff(ticks)))
        record_property("redraw_heartbeat_max_gap_seconds", maximum_gap)
        assert maximum_gap < 0.5
        assert len(rendered) == before
        assert preview.canvas.redraw_timer.isActive()
        assert len(preview.canvas.findChildren(QTimer)) == 1
        if close_pending:
            preview.close()
            assert not preview.canvas.redraw_timer.isActive()
    finally:
        release.set()
        heartbeat.stop()
    qtbot.waitUntil(lambda: target.exists(), timeout=15000)
    if close_pending:
        preview.canvas.draw()
        preview.canvas.draw_idle()
        qtbot.wait(100)
        assert len(rendered) == before
    else:
        qtbot.waitUntil(lambda: len(rendered) > before, timeout=5000)
    assert not preview.canvas.redraw_timer.isActive()
    for axes, limits in zip(preview.preview.axes, preview.full_limits):
        np.testing.assert_allclose((axes.get_xlim(), axes.get_ylim()), limits)
    assert target.stat().st_size > 1000
    preview.close()
    assert not preview.canvas.redraw_timer.isActive()


def test_evicted_failed_preview_reopens_and_retries_after_many_ready_jobs(
    qtbot, tmp_path, make_window, monkeypatch
):
    from matplotlib.figure import Figure

    computations = []

    def compute(job, cancelled, progress):
        computations.append(job.label)
        return compute_job(job, cancelled, progress)

    def writer(result, summary, directory, cancelled, progress):
        if result.job.label == "failed snapshot" and directory.parent.name != "healthy":
            raise OSError("Injected full disk")
        return export.export_result(result, summary, directory, cancelled, progress)

    manager = jobs.JobManager(compute=compute, writer=writer)
    window = make_window(tmp_path / "results", manager)
    window.calculate_button.click()
    original_id = wait_for_row(qtbot, window, 0, "saved")
    qtbot.waitUntil(lambda: original_id in window.result_windows, timeout=10000)
    original = window.result_windows[original_id]
    entered, release = Event(), Event()
    real_savefig = Figure.savefig

    def hold_savefig(figure, *args, **kwargs):
        entered.set()
        release.wait(15)
        return real_savefig(figure, *args, **kwargs)

    monkeypatch.setattr(Figure, "savefig", hold_savefig)
    target = tmp_path / "export.pdf"
    monkeypatch.setattr(QFileDialog, "getSaveFileName", lambda *args: (str(target), ""))
    try:
        original.save_plot(1)
        qtbot.waitUntil(entered.is_set, timeout=10000)
        window.label.setText("failed snapshot")
        window.calculate_button.click()
        failed = wait_for_row(qtbot, window, 1, "save_failed")
        snapshot = window.pending_previews[failed]["result"]
        summary = window.pending_previews[failed]["summary"]
        for index in range(4):
            window.label.setText(f"later success {index}")
            window.calculate_button.click()
            wait_for_row(qtbot, window, index + 2, "saved")
        assert failed not in window.pending_previews
        assert failed not in window.result_windows
        window.task_list.setCurrentIndex(1)
        window.open_button.click()
        qtbot.waitUntil(lambda: failed in window.pending_previews, timeout=5000)
        assert window.pending_previews[failed]["result"] is snapshot
        assert window.pending_previews[failed]["summary"] is summary
    finally:
        release.set()
    qtbot.waitUntil(lambda: target.exists() and failed in window.result_windows, timeout=15000)
    preview = window.result_windows[failed]
    assert preview.retry_button.isVisible()
    assert "Injected full disk" in preview.status.text()
    healthy = tmp_path / "healthy"
    healthy.mkdir()
    monkeypatch.setattr(QFileDialog, "getExistingDirectory", lambda *args: str(healthy))
    preview.retry_button.click()
    wait_for_row(qtbot, window, 1, "saved")
    assert computations.count("failed snapshot") == 1
    assert preview.result.parameter_density is snapshot.parameter_density
    assert not snapshot.parameter_density.flags.writeable
    loaded = export.load_result(manager.handles[failed].directory)
    np.testing.assert_array_equal(loaded.parameter_density, snapshot.parameter_density)
