"""Small editors for detector groups and physical grid steps."""

import math
from dataclasses import replace

from multipolepdm.grid import recommend_grid
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTableWidget,
    QVBoxLayout,
    QWidget,
)


class CompactNumber(QDoubleSpinBox):
    def textFromValue(self, value):
        return self.locale().toString(value, "g", 12)

    def wheelEvent(self, event):
        # Ignore even while focused, so Qt can deliver the wheel to an outer
        # table/scroll area. Keyboard stepping and the arrow buttons stay active.
        event.ignore()


def number(lower, upper, value, step=0.1):
    widget = CompactNumber()
    widget.setDecimals(17)
    widget.setRange(lower, upper)
    widget.setSingleStep(step)
    widget.setValue(value)
    return widget


class DetectorGroupEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.select_azimuth = False
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Theta (deg)", "Phi (deg)", "Weight"])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
        buttons = QHBoxLayout()
        add = QPushButton("+ Detector")
        remove = QPushButton("- Selected")
        add.clicked.connect(lambda: self.add_row())
        remove.clicked.connect(self.remove_row)
        buttons.addWidget(add)
        buttons.addWidget(remove)
        buttons.addStretch()
        layout.addLayout(buttons)
        self.add_row()

    def add_row(self, theta=90.0, phi=0.0, weight=1.0):
        row = self.table.rowCount()
        self.table.insertRow(row)
        for column, widget in enumerate(
            (
                number(0, 180, theta, 1),
                number(-360, 360, phi, 1),
                number(0, 1e9, weight),
            )
        ):
            self.table.setCellWidget(row, column, widget)
        self.table.cellWidget(row, 1).setEnabled(self.select_azimuth)
        self.fit_height()

    def fit_height(self):
        content = self.table.horizontalHeader().height() + 4
        content += sum(self.table.rowHeight(r) for r in range(self.table.rowCount()))
        self.table.setFixedHeight(min(180, content))

    def remove_row(self):
        if self.table.rowCount() > 1:
            row = self.table.currentRow()
            self.table.removeRow(row if row >= 0 else self.table.rowCount() - 1)
            self.fit_height()

    def set_azimuth(self, selected):
        self.select_azimuth = bool(selected)
        for row in range(self.table.rowCount()):
            self.table.cellWidget(row, 1).setEnabled(selected)

    def set_directions(self, directions):
        self.table.setRowCount(0)
        for direction in directions:
            self.add_row(direction.theta_deg, direction.phi_deg, direction.weight)

    def group(self, normalization):
        from multipolepdm.physics.detectors import DetectorDirection, DetectorGroup

        return DetectorGroup(
            tuple(
                DetectorDirection(
                    *(self.table.cellWidget(r, c).value() for c in range(3))
                )
                for r in range(self.table.rowCount())
            ),
            normalization=normalization,
        )


class GridEditor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.reference_spin = 1.0
        self._spec = recommend_grid(self.reference_spin)
        self._updating = False
        form = QFormLayout(self)
        form.setContentsMargins(0, 0, 0, 0)
        self.recommended = QCheckBox("Use recommended grid")
        self.recommended.setChecked(True)
        form.addRow(self.recommended)
        self.angle_unit = QComboBox()
        self.angle_unit.addItems(["deg", "rad"])
        form.addRow("arctan(delta) units", self.angle_unit)
        self.width_unit = QComboBox()
        self.width_unit.addItems(["sigma/I", "sigma"])
        self.values = {}
        for axis in ("angle", "width"):
            row = QHBoxLayout()
            for key in ("min", "max", "step"):
                box = number(
                    -1e4 if axis == "angle" and key != "step" else 1e-10,
                    1e4, 1,
                    0.1 if axis == "angle" else 0.005,
                )
                self.values[f"{axis}_{key}"] = box
                box.setDecimals(323)
                row.addWidget(box)
                box.valueChanged.connect(
                    lambda value, axis=axis: self._edit_axis(axis)
                )
            form.addRow(
                "arctan(delta): min / max / step"
                if axis == "angle" else "Width: min / max / step", row,
            )
            if axis == "angle":
                form.addRow("Width units", self.width_unit)
        self.hint = QLabel()
        self.hint.setWordWrap(True)
        form.addRow(self.hint)
        self.recommended.toggled.connect(self._toggle_recommended)
        self.angle_unit.currentTextChanged.connect(self.change_angle_unit)
        self.width_unit.currentTextChanged.connect(self.change_width_unit)
        self._toggle_recommended(True)

    def _toggle_recommended(self, checked):
        for box in self.values.values():
            box.setEnabled(not checked)
        if checked:
            self._restore_recommended()
        self._render()

    def _restore_recommended(self):
        try:
            self._spec = replace(
                recommend_grid(self.reference_spin),
                xi_input_unit=self.angle_unit.currentText(),
                sigma_input_unit=self.width_unit.currentText(),
            )
        except ValueError:
            # Spin fields can be temporarily invalid while typing. Keep the
            # last display, and let spec()/the hint report the actual problem.
            pass

    def _edit_axis(self, axis):
        if self._updating:
            return
        if self.recommended.isChecked():
            self._render()
            return
        lo, hi, step = (self.values[f"{axis}_{key}"].value()
                        for key in ("min", "max", "step"))
        if axis == "angle":
            scale = math.pi / 180 if self.angle_unit.currentText() == "deg" else 1
            self._spec = replace(self._spec, xi_min_rad=lo * scale,
                                 xi_max_rad=hi * scale, xi_step_rad=step * scale)
        else:
            scale = self.reference_spin if self.width_unit.currentText() == "sigma/I" else 1
            self._spec = replace(self._spec, sigma_min=lo * scale,
                                 sigma_max=hi * scale, sigma_step=step * scale)
        self.update_hint()

    def change_angle_unit(self, unit):
        if not self._updating:
            self._spec = replace(self._spec, xi_input_unit=unit)
            self._render()

    def change_width_unit(self, unit):
        if not self._updating:
            self._spec = replace(self._spec, sigma_input_unit=unit)
            self._render()

    def set_reference_spin(self, spin, reset_bounds=False):
        # reset_bounds is retained for existing callers. Only recommended mode
        # changes physical bounds; a manual/imported grid stays in absolute sigma.
        self.reference_spin = spin
        if self.recommended.isChecked():
            self._restore_recommended()
        self._render()

    def spec(self):
        if self.recommended.isChecked():
            # Validate temporary spin edits without replacing an imported,
            # physically equivalent count-defined grid.
            recommend_grid(self.reference_spin)
        return self._spec

    def load_spec(self, spec, reference_spin):
        # Compare physical axes, not metadata/point counts: legacy count-defined
        # grids must retain their exact contract when imported without editing.
        import numpy as np

        axes = spec.axes(reference_spin)
        recommended_axes = recommend_grid(reference_spin).axes(reference_spin)
        matches = all(a.shape == b.shape and np.allclose(a, b, rtol=2e-14, atol=1e-15)
                      for a, b in zip(axes, recommended_axes))
        self._updating = True
        try:
            self.reference_spin = reference_spin
            self._spec = spec
            self.recommended.blockSignals(True)
            self.recommended.setChecked(matches)
            self.recommended.blockSignals(False)
            self.angle_unit.setCurrentText(spec.xi_input_unit)
            self.width_unit.setCurrentText(spec.sigma_input_unit)
            for box in self.values.values():
                box.setEnabled(not matches)
        finally:
            self._updating = False
        self._render()

    def _display_values(self):
        spec = self._spec
        lo = spec.sigma_min
        if lo is None:
            lo = 0.15 if self.reference_spin % 1 == 0 else 0.20
        hi = self.reference_spin if spec.sigma_max is None else spec.sigma_max
        a = 180 / math.pi if spec.xi_input_unit == "deg" else 1
        s = self.reference_spin if spec.sigma_input_unit == "sigma/I" else 1
        # Zero spin is an invalid scan, but must remain an editable GUI state.
        s = s or 1
        return {
            "angle_min": spec.xi_min_rad * a,
            "angle_max": spec.xi_max_rad * a,
            "angle_step": (spec.xi_step_rad if spec.xi_step_rad is not None else
                        (spec.xi_max_rad - spec.xi_min_rad) / (spec.xi_points - 1)) * a,
            "width_min": lo / s, "width_max": hi / s,
            "width_step": (spec.sigma_step if spec.sigma_step is not None else
                        (hi - lo) / (spec.sigma_points - 1)) / s,
        }

    def _render(self):
        self._updating = True
        try:
            for key, value in self._display_values().items():
                box = self.values[key]
                lower = -1e4 if key.startswith("angle_") and key != "angle_step" else min(1e-10, value)
                box.setRange(lower, max(1e4, value))
                box.setValue(value)
        finally:
            self._updating = False
        self.update_hint()

    def update_hint(self):
        if not hasattr(self, "hint"):
            return
        note = ("Recommended grid; bounds and steps are locked. "
                if self.recommended.isChecked() else
                "Manual grid: check coverage and precision; finer steps increase runtime. "
                "Recheck Use recommended grid to replace these values. ")
        try:
            xi, sigma = self.spec().axes(self.reference_spin)
            detail = (f"{len(xi)} x {len(sigma)} nodes. "
                      f"Source sigma: {sigma[0]:g} to {sigma[-1]:g}. "
                      "Requested steps are preserved; the final cell may be shorter.")
        except ValueError as exc:
            detail = str(exc)
        self.hint.setText(note + detail)
