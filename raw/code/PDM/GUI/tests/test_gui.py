"""Real offscreen Qt widgets and calculation chain, not a mocked GUI."""

import pytest
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QFileDialog

from multipolepdm.gui.window import MainWindow
from multipolepdm.io.input import load_jobs


def test_input_modes_and_json_save(qtbot, tmp_path, monkeypatch):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.mode.setCurrentText("P_DCO")
    window.load_example()
    assert not window.gate_box.isHidden()
    assert window.pgate_box.isHidden()
    window.mode.setCurrentText("PDCO")
    assert not window.pgate_box.isHidden()
    window.file_mode.setChecked(True)
    assert not window.manual.isEnabled()
    assert not window.mode.isEnabled()
    window.file_mode.setChecked(False)
    monkeypatch.setattr(
        QFileDialog,
        "getSaveFileName",
        lambda *args: (str(tmp_path / "saved.json"), "JSON"),
    )
    window.save_json()
    assert load_jobs(tmp_path / "saved.json")[0].mode == "PDCO"
    window.close()


@pytest.mark.parametrize("mode", ["P_ADO", "P_DCO", "PDCO"])
def test_real_mode_compute_preview_save_and_exports(qtbot, tmp_path, monkeypatch, mode):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.mode.setCurrentText(mode)
    window.load_example()
    window.grid_editor.recommended.setChecked(False)
    window.grid_editor.values["angle_step"].setValue(1.0)
    window.grid_editor.values["width_step"].setValue(0.025)
    window.output_path.setText(str(tmp_path / "output"))
    qtbot.mouseClick(window.calculate_button, Qt.MouseButton.LeftButton)
    assert window.manual.isEnabled() and window.calculate_button.isEnabled()
    qtbot.waitUntil(lambda: len(window.manager.handles) == 1, timeout=3000)
    identifier = next(iter(window.manager.handles))
    qtbot.waitUntil(lambda: identifier in window.result_windows, timeout=30000)
    qtbot.waitUntil(
        lambda: window.manager.handles[identifier].state == "saved", timeout=30000
    )
    results = window.result_windows[identifier]
    assert len(results.preview.axes) == 4
    for index, suffix in [(0, "pdf"), (1, "png"), (2, "svg"), (3, "pdf"), (4, "pdf")]:
        target = tmp_path / f"panel-{index}.{suffix}"
        monkeypatch.setattr(
            QFileDialog, "getSaveFileName", lambda *args, p=str(target): (p, "")
        )
        results.save_plot(index)
        qtbot.waitUntil(lambda: target.exists(), timeout=15000)
        assert target.stat().st_size > 1000
    results.grab().save(str(tmp_path / f"{mode}-results.png"))
    window.grab().save(str(tmp_path / f"{mode}-inputs.png"))
    assert (window.manager.handles[identifier].directory / "manifest.json").exists()
    window.close()
