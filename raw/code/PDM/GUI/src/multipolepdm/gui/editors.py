"""Small editors for detector groups and physical grid steps."""

import math

from PySide6.QtWidgets import (
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
        self._angle_unit = "deg"
        self._width_unit = "sigma/I"
        form = QFormLayout(self)
        form.setContentsMargins(0, 0, 0, 0)
        self.angle_unit = QComboBox()
        self.angle_unit.addItems(["deg", "rad"])
        form.addRow("arctan(delta) units", self.angle_unit)
        self.width_unit = QComboBox()
        self.width_unit.addItems(["sigma/I", "sigma"])
        self.values = {}
        for axis, defaults in (
            ("angle", (-89.9, 89.9, 0.1)),
            ("width", (0.15, 1.0, 0.005)),
        ):
            row = QHBoxLayout()
            for key, value in zip(("min", "max", "step"), defaults):
                box = number(
                    -1e4 if axis == "angle" and key != "step" else 1e-10,
                    1e4,
                    value,
                    0.1 if axis == "angle" else 0.005,
                )
                self.values[f"{axis}_{key}"] = box
                box.setDecimals(323)
                row.addWidget(box)
                box.valueChanged.connect(self.update_hint)
            form.addRow(
                "arctan(delta): min / max / step"
                if axis == "angle"
                else "Width: min / max / step",
                row,
            )
            if axis == "angle":
                form.addRow("Width units", self.width_unit)
        self.hint = QLabel()
        self.hint.setWordWrap(True)
        form.addRow(self.hint)
        self.angle_unit.currentTextChanged.connect(self.change_angle_unit)
        self.width_unit.currentTextChanged.connect(self.change_width_unit)
        self.update_hint()

    def change_angle_unit(self, unit):
        factor = math.pi / 180 if unit == "rad" else 180 / math.pi
        if unit != self._angle_unit:
            for key in ("min", "max", "step"):
                box = self.values[f"angle_{key}"]
                converted = box.value() * factor
                lower = min(1e-10, converted) if key == "step" else -1e4
                box.setRange(lower, max(1e4, converted))
                box.setValue(converted)
            self._angle_unit = unit
        self.update_hint()

    def change_width_unit(self, unit):
        if unit != self._width_unit and self.reference_spin > 0:
            factor = self.reference_spin if unit == "sigma" else 1 / self.reference_spin
            for key in ("min", "max", "step"):
                box = self.values[f"width_{key}"]
                converted = box.value() * factor
                # Rebase limits instead of repeatedly scaling limits with a
                # possibly different reference spin on each unit switch.
                box.setRange(min(1e-10, converted), max(1e4, converted))
                box.setValue(converted)
        self._width_unit = unit
        self.update_hint()

    def set_reference_spin(self, spin, reset_bounds=False):
        self.reference_spin = spin
        if reset_bounds and spin > 0:
            scale = spin if self.width_unit.currentText() == "sigma/I" else 1
            self.values["width_min"].setValue((0.15 if spin % 1 == 0 else 0.2) / scale)
            self.values["width_max"].setValue(spin / scale)
        self.update_hint()

    def spec(self):
        from multipolepdm.contracts import GridSpec

        a = math.pi / 180 if self.angle_unit.currentText() == "deg" else 1
        s = self.reference_spin if self.width_unit.currentText() == "sigma/I" else 1
        v = {k: box.value() for k, box in self.values.items()}
        return GridSpec(
            xi_min_rad=v["angle_min"] * a,
            xi_max_rad=v["angle_max"] * a,
            xi_step_rad=v["angle_step"] * a,
            sigma_min=v["width_min"] * s,
            sigma_max=v["width_max"] * s,
            sigma_step=v["width_step"] * s,
            xi_input_unit=self.angle_unit.currentText(),
            sigma_input_unit=self.width_unit.currentText(),
        )

    def load_spec(self, spec, reference_spin):
        self.reference_spin = reference_spin
        self.angle_unit.setCurrentText(spec.xi_input_unit)
        self.width_unit.setCurrentText(spec.sigma_input_unit)
        xi, sigma = spec.axes(reference_spin)
        a = 180 / math.pi if self.angle_unit.currentText() == "deg" else 1
        s = reference_spin if self.width_unit.currentText() == "sigma/I" else 1
        values = dict(
            angle_min=xi[0] * a,
            angle_max=xi[-1] * a,
            angle_step=(spec.xi_step_rad or (xi[1] - xi[0])) * a,
            width_min=sigma[0] / s,
            width_max=sigma[-1] / s,
            width_step=(spec.sigma_step or (sigma[1] - sigma[0])) / s,
        )
        for k, v in values.items():
            self.values[k].setValue(v)
        self.update_hint()

    def update_hint(self):
        if not hasattr(self, "hint"):
            return
        counts = []
        for axis in ("angle", "width"):
            lo, hi, step = (
                self.values[f"{axis}_{k}"].value() for k in ("min", "max", "step")
            )
            counts.append(max(0, math.ceil((hi - lo) / step - 1e-9) + 1))
        self.hint.setText(
            f"Approx. {counts[0]} x {counts[1]} nodes. "
            "Requested steps are preserved; the final cell may be shorter."
        )
