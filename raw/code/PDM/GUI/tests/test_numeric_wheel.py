"""Wheel safety through the shared number editor, including focused table cells."""

import pytest
from multipolepdm.gui.editors import DetectorGroupEditor, number
from multipolepdm.gui.window import MainWindow
from PySide6.QtCore import QPoint, QPointF, Qt
from PySide6.QtGui import QWheelEvent
from PySide6.QtTest import QTest
from PySide6.QtWidgets import QApplication, QScrollArea, QVBoxLayout, QWidget


def wheel(widget, delta=120):
    pos = widget.rect().center()
    event = QWheelEvent(
        QPointF(pos), QPointF(widget.mapToGlobal(pos)), QPoint(), QPoint(0, delta),
        Qt.MouseButton.NoButton, Qt.KeyboardModifier.NoModifier,
        Qt.ScrollPhase.NoScrollPhase, False,
    )
    QApplication.sendEvent(widget, event)
    return event


@pytest.mark.parametrize("focused", [False, True])
def test_all_numbers_ignore_wheel_including_table_cells(qtbot, focused):
    window = MainWindow()
    qtbot.addWidget(window)
    window.show()
    window.grid_editor.recommended.setChecked(False)
    for editor in window.group_editors.values():
        editor.add_row(55, 30, 0.7)
    boxes = list(window.fields.values()) + list(window.grid_editor.values.values())
    for editor in window.group_editors.values():
        boxes.extend(editor.table.cellWidget(r, c)
                     for r in range(editor.table.rowCount()) for c in range(3))
    for box in boxes:
        box.setFocus() if focused else box.clearFocus()
        before = box.value()
        for receiver in (box, box.lineEdit()):
            for delta in (-120, 120):
                wheel(receiver, delta)
                assert box.value() == before
    window.close()


def test_keyboard_and_buttons_still_change_value(qtbot):
    box = number(0, 100, 5, 1)
    qtbot.addWidget(box)
    box.show()
    box.setFocus()
    qtbot.keyClick(box, Qt.Key.Key_Up)
    assert box.value() == 6
    qtbot.keyClick(box, Qt.Key.Key_Down)
    assert box.value() == 5
    qtbot.mouseClick(box, Qt.MouseButton.LeftButton,
                     pos=QPoint(box.width() - 5, box.height() // 4))
    assert box.value() == 6


def test_focused_number_allows_outer_scroll(qtbot):
    scroll = QScrollArea()
    qtbot.addWidget(scroll)
    body = QWidget()
    layout = QVBoxLayout(body)
    box = number(0, 100, 5)
    layout.addWidget(box)
    layout.addStretch()
    body.setMinimumHeight(2000)
    scroll.setWidget(body)
    scroll.resize(300, 200)
    scroll.show()
    box.setFocus()
    qtbot.waitUntil(lambda: scroll.verticalScrollBar().maximum() > 0)
    qtbot.waitUntil(box.hasFocus)
    QTest.wheelEvent(scroll.windowHandle(), box.mapTo(scroll, box.rect().center()),
                     QPoint(0, -120))
    QApplication.processEvents()
    assert box.value() == 5
    assert scroll.verticalScrollBar().value() > 0


def test_focused_table_number_scrolls_table_without_editing(qtbot):
    editor = DetectorGroupEditor()
    qtbot.addWidget(editor)
    for _ in range(12):
        editor.add_row()
    editor.show()
    box = editor.table.cellWidget(0, 0)
    box.setFocus()
    qtbot.waitUntil(box.hasFocus)
    before = box.value()
    QTest.wheelEvent(editor.windowHandle(), box.mapTo(editor, box.rect().center()),
                     QPoint(0, -120))
    QApplication.processEvents()
    assert box.value() == before
    assert editor.table.verticalScrollBar().value() > 0
