"""Compact editor with independent calculation, preview and save lifecycles."""

import json
from collections import deque
from dataclasses import replace
from queue import Empty
from threading import Thread

from multipolepdm.contracts import (
    Geometry,
    JobRequest,
    Measurement,
    OutputSpec,
    Transition,
)
from multipolepdm.grid import recommend_grid
from multipolepdm.gui.editors import CompactNumber, DetectorGroupEditor, GridEditor
from multipolepdm.io.input import example_data, job_from_dict, load_jobs, save_input
from multipolepdm.jobs.manager import JobManager, QueueFull
from multipolepdm.models.registry import MODE_CONFIGS
from multipolepdm.physics.detectors import DetectorDirection
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPlainTextEdit,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    MAX_PENDING_PREVIEWS = 3

    def __init__(self, manager=None):
        super().__init__()
        self.setWindowTitle("PDM")
        self.resize(800, 900)
        self.manager = manager or JobManager()
        self.result_windows = {}
        self.pending_previews = {}
        self.opening_job = None
        self.task_rows = {}
        self.fields = {}
        self.pending_jobs = deque()
        root = QWidget()
        self.setCentralWidget(root)
        layout = QVBoxLayout(root)
        title = QLabel("PDM | Nuclear multipole mixing")
        title.setStyleSheet("font-size: 20px; font-weight: 600;")
        layout.addWidget(title)
        self.mode = QComboBox()
        self.mode.addItems(MODE_CONFIGS)
        layout.addWidget(self.mode)
        self.description = QLabel()
        layout.addWidget(self.description)
        source = QHBoxLayout()
        layout.addLayout(source)
        self.file_mode = QCheckBox("Input JSON file")
        source.addWidget(self.file_mode)
        self.file_path = QLineEdit()
        self.file_path.setPlaceholderText("Single job or batch JSON")
        source.addWidget(self.file_path)
        choose = QPushButton("Browse")
        choose.clicked.connect(self.choose_file)
        source.addWidget(choose)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll, 1)
        body = QWidget()
        scroll.setWidget(body)
        body_layout = QVBoxLayout(body)
        self.manual = QWidget()
        body_layout.addWidget(self.manual)
        form = QFormLayout(self.manual)
        self.label = QLineEdit("Transition")
        form.addRow("Label", self.label)
        target = QHBoxLayout()
        for key in ("target_initial", "target_final"):
            target.addWidget(self.number(key, 0, 100, 0.5))
        form.addRow("Target spin: initial / final", target)
        self.multipoles = QComboBox()
        self.multipoles.addItems(["M1 + E2"])
        form.addRow("Target multipoles", self.multipoles)
        for obs in ("P", "ratio"):
            line = QHBoxLayout()
            for part in ("value", "err_minus", "err_plus"):
                key = f"{obs}_{part}"
                line.addWidget(
                    self.number(
                        key, -10000 if part == "value" else 0.000001, 10000, 0.01
                    )
                )
            label = QLabel(
                "P: value / -error / +error"
                if obs == "P"
                else "R_ADO: value / -error / +error"
            )
            form.addRow(label, line)
            if obs == "ratio":
                self.ratio_label = label
        self.select_azimuth = QCheckBox("Select ratio azimuth (otherwise average full rings)")
        form.addRow(self.select_azimuth)
        self.group_normalization = QComboBox()
        self.group_normalization.addItem("Relative weighted mean", "mean")
        self.group_normalization.addItem("Raw weighted sum", "sum")
        form.addRow("Detector weights", self.group_normalization)
        self.group_editors = {}
        for key, label in (
            ("ratio_group_a", "Ratio group A"),
            ("ratio_group_b", "Ratio group B"),
            ("polarization_group", "Polarization target group"),
        ):
            editor = DetectorGroupEditor()
            self.group_editors[key] = editor
            form.addRow(label, editor)
        geometry_note = QLabel(
            "R_ADO = W(A)/W(B); R_DCO = C(target A, gate B)/C(target B, gate A)."
        )
        geometry_note.setWordWrap(True)
        form.addRow(geometry_note)
        self.gate_box = QGroupBox("DCO path")
        gate_form = QFormLayout(self.gate_box)
        form.addRow(self.gate_box)
        self.target_first = QComboBox()
        self.target_first.addItems(
            ["Target first, gate later", "Gate first, target later"]
        )
        gate_form.addRow("Emission order", self.target_first)
        gate_spins = QHBoxLayout()
        for key in ("gate_initial", "gate_final"):
            gate_spins.addWidget(self.number(key, 0, 100, 0.5))
        gate_form.addRow("Gate spin: initial / final", gate_spins)
        self.gate_multipoles = QComboBox()
        self.gate_multipoles.addItems(["E2", "M1", "E1", "M2", "M1 + E2"])
        gate_form.addRow("Gate multipoles", self.gate_multipoles)
        gate_form.addRow(
            "Gate delta (mixed gate only)",
            self.number("gate_delta", -10000, 10000, 0.1),
        )
        self.pgate_box = QGroupBox("Polarization direction gate")
        self.select_polarization_azimuth = QCheckBox(
            "Select PDCO polarization azimuth (target and gate)"
        )
        self.select_polarization_azimuth.setToolTip(
            "Unchecked: average target/gate intensities over azimuth at each polar angle. "
            "Independent of the ratio azimuth selection."
        )
        form.addRow(self.select_polarization_azimuth)
        pgate = QFormLayout(self.pgate_box)
        gate_form.addRow(self.pgate_box)
        self.group_editors["polarization_gate_group"] = DetectorGroupEditor()
        pgate.addRow(
            "Gate detector group", self.group_editors["polarization_gate_group"]
        )
        self.select_azimuth.toggled.connect(self.update_azimuth)
        self.select_polarization_azimuth.toggled.connect(self.update_azimuth)
        self.grid_editor = GridEditor()
        grid_box = QGroupBox("Parameter grid")
        grid_layout = QVBoxLayout(grid_box)
        grid_layout.addWidget(self.grid_editor)
        form.addRow(grid_box)
        advanced = QGroupBox("Advanced parameters")
        advanced.setCheckable(True)
        advanced.setChecked(False)
        self.advanced = advanced
        advanced_layout = QVBoxLayout(advanced)
        advanced_content = QWidget()
        advanced_layout.addWidget(advanced_content)
        advanced_form = QFormLayout(advanced_content)
        form.addRow(advanced)
        advanced_content.setVisible(False)
        advanced.toggled.connect(advanced_content.setVisible)
        self.intermediates = QPlainTextEdit("[]")
        self.intermediates.setMaximumHeight(75)
        self.intermediates.setPlaceholderText(
            "Intermediate transitions as JSON array; [] for adjacent lines"
        )
        advanced_form.addRow("Unobserved intermediate path", self.intermediates)
        destination = QHBoxLayout()
        layout.addLayout(destination)
        self.output_path = QLineEdit("pdm-results")
        destination.addWidget(QLabel("Output folder"))
        destination.addWidget(self.output_path)
        out_button = QPushButton("Browse")
        out_button.clicked.connect(self.choose_output)
        destination.addWidget(out_button)
        self.full_csv = QCheckBox("Also export full grid CSV (larger and slower)")
        layout.addWidget(self.full_csv)
        actions = QHBoxLayout()
        layout.addLayout(actions)
        self.example_button = QPushButton("Load example")
        self.example_button.clicked.connect(self.load_example)
        actions.addWidget(self.example_button)
        self.save_button = QPushButton("Save input JSON")
        self.save_button.clicked.connect(self.save_json)
        actions.addWidget(self.save_button)
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        actions.addWidget(self.calculate_button)
        self.progress = QProgressBar()
        layout.addWidget(self.progress)
        self.status = QLabel(
            "Ready. Select a mode and enter final measured quantities."
        )
        self.status.setWordWrap(True)
        layout.addWidget(self.status)
        self.task_list = QComboBox()
        layout.addWidget(self.task_list)
        self.open_button = QPushButton("Open selected result")
        self.open_button.clicked.connect(self.open_selected_result)
        layout.addWidget(self.open_button)
        cancel = QPushButton("Cancel selected task")
        cancel.clicked.connect(self.cancel_task)
        layout.addWidget(cancel)
        self.mode.currentTextChanged.connect(self.update_mode)
        self.file_mode.toggled.connect(self.update_source)
        for key in ("target_initial", "gate_initial"):
            self.fields[key].valueChanged.connect(self.refresh_sigma_defaults)
        self.target_first.currentIndexChanged.connect(self.refresh_sigma_defaults)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.process_events)
        self.timer.start(50)
        self.load_example()
        self.update_source()

    def number(self, key, lo, hi, step):
        box = CompactNumber()
        box.setDecimals(12)
        box.setRange(lo, hi)
        box.setSingleStep(step)
        self.fields[key] = box
        return box

    def update_azimuth(self, *args):
        ratio_selected = self.select_azimuth.isChecked()
        polar_selected = (
            self.select_polarization_azimuth.isChecked()
            if self.mode.currentText() == "PDCO" else ratio_selected
        )
        for name, editor in self.group_editors.items():
            editor.set_azimuth(ratio_selected if name.startswith("ratio_") else polar_selected)

    def update_mode(self, *args):
        mode = self.mode.currentText()
        self.description.setText(MODE_CONFIGS[mode].DESCRIPTION)
        self.gate_box.setVisible(mode != "P_ADO")
        self.pgate_box.setVisible(mode == "PDCO")
        self.select_polarization_azimuth.setVisible(mode == "PDCO")
        self.update_azimuth()
        self.ratio_label.setText(
            ("R_ADO" if mode == "P_ADO" else "R_DCO") + ": value / -error / +error"
        )
        self.refresh_sigma_defaults()

    def refresh_sigma_defaults(self, *args):
        ref = (
            self.fields["target_initial"].value()
            if self.mode.currentText() == "P_ADO"
            or self.target_first.currentIndex() == 0
            else self.fields["gate_initial"].value()
        )
        self.grid_editor.set_reference_spin(ref)

    def update_source(self, *args):
        from_file = self.file_mode.isChecked()
        self.manual.setEnabled(not from_file)
        self.file_path.setEnabled(from_file)
        self.mode.setEnabled(not from_file)
        self.example_button.setEnabled(not from_file)
        self.save_button.setEnabled(not from_file)

    def load_example(self):
        job = job_from_dict(example_data(self.mode.currentText()))
        self.label.setText(job.label)
        values = {
            "target_initial": job.target.spin_initial,
            "target_final": job.target.spin_final,
        }
        for name, obs in (("P", job.polarization), ("ratio", job.angular_ratio)):
            for part in ("value", "err_minus", "err_plus"):
                values[f"{name}_{part}"] = getattr(obs, part)
        gate = job.gate or Transition(4, 2, ("E2",))
        values.update(
            gate_initial=gate.spin_initial,
            gate_final=gate.spin_final,
            gate_delta=gate.delta,
        )
        for key, value in values.items():
            self.fields[key].setValue(value)
        geometry = job.geometry
        self.select_azimuth.setChecked(
            geometry.select_azimuth and not geometry.ratio_azimuth_average
        )
        self.select_polarization_azimuth.setChecked(
            geometry.select_azimuth and not geometry.polarization_gate_azimuth_average
        )
        fallback = {
            "ratio_group_a": DetectorDirection(geometry.theta_a_deg),
            "ratio_group_b": DetectorDirection(
                geometry.theta_b_deg, geometry.relative_phi_deg
            ),
            "polarization_group": DetectorDirection(
                geometry.theta_p_deg, geometry.phi_p_deg
            ),
            "polarization_gate_group": DetectorDirection(
                geometry.theta_gate_p_deg, geometry.phi_gate_p_deg
            ),
        }
        for key, editor in self.group_editors.items():
            group = getattr(geometry, key)
            editor.set_directions(group.directions if group else (fallback[key],))
        normalizations = {
            getattr(geometry, k).normalization
            for k in self.group_editors
            if getattr(geometry, k) is not None
        }
        self.group_normalization.setCurrentIndex(1 if normalizations == {"sum"} else 0)
        self.gate_multipoles.setCurrentText(" + ".join(gate.multipoles))
        self.target_first.setCurrentIndex(0 if job.target_first else 1)
        self.intermediates.setPlainText("[]")
        self.update_mode()
        self.grid_editor.load_spec(recommend_grid(job.reference_spin), job.reference_spin)

    def read_job(self):
        def value(key):
            field = self.fields[key]
            return field.isChecked() if isinstance(field, QCheckBox) else field.value()

        mode = self.mode.currentText()
        obs = lambda name: Measurement(
            *(value(f"{name}_{p}") for p in ("value", "err_minus", "err_plus"))
        )
        gate = (
            None
            if mode == "P_ADO"
            else Transition(
                value("gate_initial"),
                value("gate_final"),
                tuple(self.gate_multipoles.currentText().split(" + ")),
                value("gate_delta"),
            )
        )
        intermediates = (
            ()
            if mode == "P_ADO"
            else tuple(
                Transition(**t) for t in json.loads(self.intermediates.toPlainText())
            )
        )
        ratio_selected = self.select_azimuth.isChecked()
        polar_selected = mode == "PDCO" and self.select_polarization_azimuth.isChecked()
        job = JobRequest(
            mode,
            Transition(value("target_initial"), value("target_final")),
            obs("P"),
            obs("ratio"),
            label=self.label.text(),
            gate=gate,
            target_first=self.target_first.currentIndex() == 0,
            intermediates=intermediates,
            geometry=Geometry(
                select_azimuth=ratio_selected or polar_selected,
                ratio_azimuth_average=not ratio_selected,
                polarization_gate_azimuth_average=not polar_selected,
                **{
                    key: editor.group(self.group_normalization.currentData())
                    for key, editor in self.group_editors.items()
                    if key != "polarization_gate_group" or mode == "PDCO"
                },
            ),
            grid=self.grid_editor.spec(),
            output=OutputSpec(self.output_path.text(), self.full_csv.isChecked()),
        )
        job.grid.axes(job.reference_spin)
        return job

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Input jobs", "", "JSON (*.json)")
        if path:
            self.file_path.setText(path)
            self.file_mode.setChecked(True)

    def choose_output(self):
        path = QFileDialog.getExistingDirectory(
            self, "Output folder", self.output_path.text()
        )
        if path:
            self.output_path.setText(path)

    def save_json(self):
        try:
            job = self.read_job()
            path, _ = QFileDialog.getSaveFileName(
                self, "Save input", "example.json", "JSON (*.json)"
            )
            if path:
                save_input(job, path)
        except Exception as exc:
            QMessageBox.warning(self, "Check inputs", str(exc))

    def calculate(self):
        try:
            jobs = (
                load_jobs(self.file_path.text())
                if self.file_mode.isChecked()
                else (self.read_job(),)
            )
            # The file owns all scientific fields; only the visible destination overrides output.
            for job in jobs:
                job = replace(
                    job,
                    output=OutputSpec(
                        self.output_path.text(), self.full_csv.isChecked()
                    ),
                )
                self.pending_jobs.append(job)
            self.status.setText(
                f"Queued {len(jobs)} job(s). You can edit and submit another."
            )
            self.submit_pending()
        except Exception as exc:
            QMessageBox.warning(self, "Check inputs", str(exc))

    def submit_pending(self):
        while self.pending_jobs:
            job = self.pending_jobs[0]
            try:
                identifier = self.manager.submit(job)
            except QueueFull:
                break
            except Exception as exc:
                self.pending_jobs.popleft()
                self.task_list.addItem(job.label + " | submission failed")
                self.status.setText("Submission failed: " + str(exc))
                continue
            self.pending_jobs.popleft()
            self.task_list.addItem(job.label + " | queued", identifier)
            self.task_rows[identifier] = self.task_list.count() - 1

    def cancel_task(self):
        identifier = self.task_list.currentData()
        if identifier:
            self.manager.cancel(identifier)

    def open_selected_result(self):
        identifier = self.task_list.currentData()
        if not identifier or self.opening_job is not None:
            return
        if identifier in self.pending_previews:
            self.status.setText("Preview waiting for figure export to finish.")
            return
        window = self.result_windows.get(identifier)
        if window is not None:
            window.showNormal()
            window.raise_()
            window.activateWindow()
            return
        try:
            self.manager.open_saved(identifier)
        except RuntimeError as exc:
            self.status.setText(str(exc))
            return
        self.opening_job = identifier
        self.open_button.setEnabled(False)
        self.status.setText("Opening result...")

    def retry_data_save(self, identifier):
        window = self.result_windows[identifier]
        destination = QFileDialog.getExistingDirectory(
            window, "Choose output folder", str(window.directory.parent)
        )
        if not destination or self.result_windows.get(identifier) is not window:
            return
        try:
            self.manager.retry_save(
                identifier, window.result, window.summary, destination
            )
        except Exception as exc:
            window.show_data_state("save_failed", window.directory, str(exc))
            return
        window.show_data_state("queued", self.manager.handles[identifier].directory)

    def forget_result(self, identifier, window):
        if self.result_windows.get(identifier) is window:
            self.result_windows.pop(identifier)

    def show_result(self, identifier, event, saved=False):
        self.pending_previews.pop(identifier, None)
        if len(self.pending_previews) >= self.MAX_PENDING_PREVIEWS:
            oldest = next(iter(self.pending_previews))
            self.pending_previews.pop(oldest)
        self.pending_previews[identifier] = {
            **event,
            "state": event.get("data_state", "saved" if saved else event.get("state", "ready")),
        }
        self.process_pending_preview()

    def process_pending_preview(self):
        if not self.pending_previews:
            return
        identifier = next(iter(self.pending_previews))
        event = self.pending_previews[identifier]
        try:
            from multipolepdm.gui.results import ResultsWindow

            window = ResultsWindow.try_create(
                event["result"], event["summary"], event["directory"]
            )
            if window is None:
                return
            self.pending_previews.pop(identifier)
            window.closed.connect(lambda closed: self.forget_result(identifier, closed))
            window.retry_button.clicked.connect(
                lambda: self.retry_data_save(identifier)
            )
            if event["state"] != "ready":
                window.show_data_state(
                    event["state"], event["directory"], event.get("error", "")
                )
            if len(self.result_windows) >= 3:
                oldest = next(
                    (
                        job_id
                        for job_id in self.result_windows
                        if self.manager.handles[job_id].state in ("saved", "cancelled")
                    ),
                    next(iter(self.result_windows)),
                )
                self.result_windows.pop(oldest).close()
            self.result_windows[identifier] = window
            window.show()
        except Exception as exc:
            self.pending_previews.pop(identifier, None)
            self.status.setText("Could not display result: " + str(exc))

    def process_events(self):
        self.submit_pending()
        while True:
            try:
                event = self.manager.events.get_nowait()
            except Empty:
                break
            identifier, state = event["job_id"], event["state"]
            if state in ("opened", "open_failed"):
                self.opening_job = None
                self.open_button.setEnabled(True)
                if state == "opened":
                    self.status.setText("Opened result: " + event["directory"])
                    self.show_result(identifier, event, saved=True)
                else:
                    self.status.setText(
                        "Could not open saved result: " + event["error"]
                    )
                continue
            label = self.manager.handles[identifier].job.label
            if identifier in self.task_rows:
                self.task_list.setItemText(
                    self.task_rows[identifier], label + " | " + state
                )
            if "percent" in event:
                self.progress.setValue(round(event["percent"]))
            self.status.setText(
                label
                + " | "
                + state
                + " | "
                + event["directory"]
                + (" | " + event["error"] if "error" in event else "")
            )
            if state == "ready":
                self.show_result(identifier, event)
            elif identifier in self.pending_previews:
                self.pending_previews[identifier].update(event)
            elif identifier in self.result_windows:
                self.result_windows[identifier].show_data_state(
                    state, event["directory"], event.get("error", "")
                )
        self.process_pending_preview()

    def closeEvent(self, event):
        active = bool(self.pending_jobs) or any(
            h.state not in ("saved", "cancelled", "save_failed", "calculation_failed")
            for h in self.manager.handles.values()
        )
        if active:
            answer = QMessageBox.question(
                self,
                "Tasks active",
                "Cancel pending work and close? Completed previews and saved files are kept.",
            )
            if answer != QMessageBox.StandardButton.Yes:
                event.ignore()
                return
        self.timer.stop()
        self.pending_jobs.clear()
        self.pending_previews.clear()
        for window in list(self.result_windows.values()):
            window.close()
        Thread(
            target=self.manager.shutdown,
            kwargs={"wait": True, "cancel": True},
            daemon=False,
        ).start()
        event.accept()
