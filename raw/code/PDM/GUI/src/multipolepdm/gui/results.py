"""Scrollable, zoomable scientific preview independent of disk completion."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from queue import Empty, Queue

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT
from PySide6.QtCore import QTimer, Signal
from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QPlainTextEdit,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


def summary_text(summary):
    from multipolepdm.plotting.intervals import format_marginal, format_tan_statistics

    return "\n\n".join((
        format_tan_statistics(summary.tan_angle_statistics, summary.arctan_delta),
        format_marginal(summary.sigma_over_i),
    ))


class PreviewToolbar(NavigationToolbar2QT):
    toolitems = tuple(
        item for item in NavigationToolbar2QT.toolitems if item[3] != "save_figure"
    )


class DeferredFigureCanvas(FigureCanvasQTAgg):
    """Coalesce Qt redraw requests while another thread renders an export."""

    def __init__(self, figure):
        super().__init__(figure)
        self.redraw_closed = False
        self.redraw_timer = QTimer(self)
        self.redraw_timer.setSingleShot(True)
        self.redraw_timer.setInterval(50)
        self.redraw_timer.timeout.connect(self.draw)

    def draw(self):
        from multipolepdm.plotting.style import MATPLOTLIB_LOCK

        if self.redraw_closed:
            return
        if not MATPLOTLIB_LOCK.acquire(blocking=False):
            if not self.redraw_timer.isActive():
                self.redraw_timer.start()
            return
        try:
            self.redraw_timer.stop()
            super().draw()
        finally:
            MATPLOTLIB_LOCK.release()

    def stop_redraws(self):
        self.redraw_closed = True
        self.redraw_timer.stop()
        self._draw_pending = False

    def closeEvent(self, event):
        self.stop_redraws()
        super().closeEvent(event)


class ResultsWindow(QWidget):
    closed = Signal(object)

    @classmethod
    def try_create(cls, result, summary, directory, parent=None):
        """Return None while an export owns Matplotlib; never wait on Qt."""
        from multipolepdm.plotting.style import MATPLOTLIB_LOCK

        if not MATPLOTLIB_LOCK.acquire(blocking=False):
            return None
        try:
            return cls(result, summary, directory, parent)
        finally:
            MATPLOTLIB_LOCK.release()

    def __init__(self, result, summary, directory, parent=None):
        from multipolepdm.plotting.overview import make_preview
        from multipolepdm.plotting.style import GUI_STYLE

        super().__init__(parent)
        self.setWindowTitle(f"PDM results - {result.job.label}")
        self.resize(1050, 900)
        self.result, self.summary, self.directory = result, summary, Path(directory)
        self.export_events = Queue()
        self.exporter = ThreadPoolExecutor(
            max_workers=1, thread_name_prefix="pdm-figure-export"
        )
        self.export_timer = QTimer(self)
        self.export_timer.timeout.connect(self.process_exports)
        self.export_timer.start(100)
        self.preview = make_preview(result, summary, style=GUI_STYLE)
        self.full_limits = tuple(
            (axis.get_xlim(), axis.get_ylim()) for axis in self.preview.axes
        )
        outer = QVBoxLayout(self)
        self.status = QLabel(f"Calculation ready; data saving to {directory}")
        self.status.setWordWrap(True)
        self.status.setTextInteractionFlags(
            __import__("PySide6.QtCore", fromlist=["Qt"]).Qt.TextSelectableByMouse
        )
        outer.addWidget(self.status)
        self.retry_button = QPushButton("Retry data save...")
        self.retry_button.hide()
        outer.addWidget(self.retry_button)
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        outer.addWidget(scroll)
        content = QWidget()
        layout = QVBoxLayout(content)
        scroll.setWidget(content)
        self.canvas = DeferredFigureCanvas(self.preview.figure)
        self.canvas.setMinimumSize(
            *(round(size * self.preview.figure.dpi) for size in self.preview.figure.get_size_inches())
        )
        self.toolbar = PreviewToolbar(self.canvas, self)
        self.toolbar.setToolTip("Preview navigation")
        outer.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        view_controls = QHBoxLayout()
        layout.addLayout(view_controls)
        reset = QPushButton("Restore full ranges")
        reset.clicked.connect(self.restore_full_ranges)
        view_controls.addWidget(reset)
        buttons = QHBoxLayout()
        layout.addLayout(buttons)
        for index, label in enumerate(
            (
                "Save overview",
                "Save observation",
                "Save parameters",
                "Save arctan(delta)",
                "Save sigma/I",
            )
        ):
            button = QPushButton(label)
            button.setToolTip("Export the scientific figure from the computed data.")
            button.clicked.connect(lambda checked=False, n=index: self.save_plot(n))
            buttons.addWidget(button)
        valid = result.response.valid
        details = [
            f"Gaussian initial spin I = {result.response.reference_spin:g}\n"
            f"Invalid response nodes: {valid.size - int(valid.sum()):,} of {valid.size:,}\n"
            "Delta convention: KS/Droste\n\n" + summary_text(summary)
        ]
        groups = result.response.metadata.get("detector_groups", {})
        if groups:
            details.append("\nEffective detector weights in input order")
            labels = {
                "ratio_group_a": "Ratio group A",
                "ratio_group_b": "Ratio group B",
                "polarization_group": "Polarization group",
                "polarization_gate_group": "Polarization gate group",
            }
            for name, group in groups.items():
                weights = ", ".join(f"{row['effective_weight']:.6g}" for row in group["directions"])
                method = {"sum": "weighted sum", "mean": "weighted mean"}[group["normalization"]]
                details.append(f"{labels.get(name, name)} ({method})  [{weights}]")
        stats = QPlainTextEdit("\n".join(details))
        stats.setReadOnly(True)
        stats.setMinimumHeight(110)
        stats.setMaximumHeight(160)
        outer.addWidget(stats)
        if result.warnings:
            warning = QLabel("\n".join(result.warnings))
            warning.setWordWrap(True)
            layout.addWidget(warning)
        self.canvas.draw()

    def show_data_state(self, state, directory, error=""):
        self.directory = Path(directory)
        self.status.setText(
            f"{state}: {directory}" + (f" | {error}" if error else "")
        )
        self.retry_button.setVisible(state == "save_failed")

    def restore_full_ranges(self):
        for axes, (xlim, ylim) in zip(self.preview.axes, self.full_limits):
            axes.set_xlim(*xlim)
            axes.set_ylim(*ylim)
        self.toolbar.push_current()
        self.canvas.draw_idle()

    def process_exports(self):
        while True:
            try:
                message = self.export_events.get_nowait()
            except Empty:
                break
            self.status.setText(message)

    def save_plot(self, index):
        from multipolepdm.plotting.export import supported_formats

        filters = "Figures (" + " ".join("*." + x for x in supported_formats()) + ")"
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save scientific figure",
            str(self.directory / ("overview" if index == 0 else f"panel-{index}"))
            + ".pdf",
            filters,
        )
        if not path:
            return
        self.status.setText("Export queued: " + path)
        # Worker closures must not own Qt widgets: their final reference could
        # otherwise be released on a worker thread during window teardown.
        result, summary, events = self.result, self.summary, self.export_events

        def save():
            try:
                if index == 0:
                    from multipolepdm.plotting.export import save_overview

                    save_overview(result, summary, path)
                else:
                    from multipolepdm.plotting.export import save_panel

                    save_panel(result, summary, "abcd"[index - 1], path)
                events.put("Figure saved: " + path)
            except Exception as exc:
                events.put("Figure export failed: " + str(exc))

        self.exporter.submit(save)

    def closeEvent(self, event):
        self.canvas.stop_redraws()
        self.export_timer.stop()
        self.exporter.shutdown(wait=False)
        event.accept()
        self.closed.emit(self)
