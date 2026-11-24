"""Packaged GUI smoke test, usable with offscreen Qt or a virtual X11 display."""

import json
import os
from pathlib import Path
import platform
import time
import uuid

from PySide6.QtWidgets import QApplication

from multipolepdm.gui.window import MainWindow
from multipolepdm.plotting.export import save_overview, save_panel


def run_self_test(report_path):
    report_path = Path(report_path).resolve()
    report_path.parent.mkdir(parents=True, exist_ok=True)
    artifacts = report_path.parent / (report_path.stem + "-" + uuid.uuid4().hex[:8])
    artifacts.mkdir()
    report = {
        "kind": "real Qt packaged smoke test",
        "system": platform.system(),
        "platform_plugin": os.environ.get("QT_QPA_PLATFORM", "platform default"),
        "native_windows_macos_tested": False,
        "status": "running",
        "cases": [],
    }
    app = QApplication.instance() or QApplication([])
    window = MainWindow()
    window.show()
    try:
        window.file_mode.setChecked(True)
        assert not window.manual.isEnabled()
        window.file_mode.setChecked(False)
        for mode in ("P_ADO", "P_DCO", "PDCO"):
            window.mode.setCurrentText(mode)
            window.load_example()
            window.grid_editor.values["angle_step"].setValue(1.0)
            window.grid_editor.values["width_step"].setValue(0.025)
            window.output_path.setText(str(artifacts / "data"))
            window.calculate_button.click()
            assert window.manual.isEnabled()
            identifier = list(window.manager.handles)[-1]
            deadline = time.monotonic() + 120
            while time.monotonic() < deadline:
                app.processEvents()
                state = window.manager.handles[identifier].state
                if state in ("calculation_failed", "save_failed", "cancelled"):
                    raise RuntimeError(f"{mode}: {state}")
                if state == "saved" and identifier in window.result_windows:
                    break
                time.sleep(0.01)
            else:
                raise RuntimeError(f"{mode}: smoke-test timeout")
            result_window = window.result_windows[identifier]
            assert len(result_window.preview.axes) == 4
            result_window.grab().save(str(artifacts / f"{mode}-results.png"))
            window.grab().save(str(artifacts / f"{mode}-inputs.png"))
            save_overview(
                result_window.result, result_window.summary, artifacts / f"{mode}.pdf"
            )
            for panel in "abcd":
                save_panel(
                    result_window.result,
                    result_window.summary,
                    panel,
                    artifacts / f"{mode}-{panel}.svg",
                )
            report["cases"].append(
                {
                    "mode": mode,
                    "status": state,
                    "directory": str(window.manager.handles[identifier].directory),
                    "four_panels": True,
                    "manual_editor_enabled": True,
                }
            )
        report["status"] = "passed"
    except Exception as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
    finally:
        window.manager.shutdown(wait=True, cancel=True)
        window.close()
        app.processEvents()
        report["artifacts"] = str(artifacts)
        report_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return 0 if report["status"] == "passed" else 1
