from PyQt6.QtWidgets import QColorDialog, QPushButton
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QSettings
from PyQt6.QtCore import pyqtSignal

class ColorButton(QPushButton):
    color_changed = pyqtSignal(QColor)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet("background-color: black;")
        self.current_color = QColor(0, 0, 0)
        
        self.settings = QSettings('mdelbranson', 'mathnasium-demo')
        self.load_custom_colors()

    def load_custom_colors(self):
        for i in range(QColorDialog.customCount()):
            key = f'CustomColors/color{i}'
            if self.settings.contains(key):
                color = QColor(self.settings.value(key))
                QColorDialog.setCustomColor(i, color.rgb())

    def save_custom_colors(self):
        for i in range(QColorDialog.customCount()):
            color = QColorDialog.customColor(i)
            self.settings.setValue(f'CustomColors/color{i}', color.name())

    def mousePressEvent(self, event):
        color = QColorDialog.getColor()
        if color.isValid():
            self.setStyleSheet(f"background-color: {color.name()};")
            self.current_color = color
            self.save_custom_colors()
            self.color_changed.emit(color)
