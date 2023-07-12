from src.gui.modes.mode_base import AbstractMode
from src.gui.modes.presentation_mode.presentation_view import PresentationView
from src.gui.modes.presentation_mode.presentation_controls_widget import Ui_Form as PresentationControlUI
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui, QtCore

class PresentationMode(AbstractMode):
    def __init__(self, parent):
        super().__init__(parent=parent,
                        description="Presentation Mode", 
                         icon_filename="mode-present.ico", 
                         display=PresentationView(), 
                         control_ui=PresentationControlUI())        
        
        self.presentations_tool_bar = QtWidgets.QToolBar(parent=self.parent)
        self.presentations_tool_bar.setFloatable(False)
        self.presentations_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.presentations_tool_bar.setHidden(False)
        self.parent.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.presentations_tool_bar)
        
        self.tool_bars = {
            "Presentations": self.presentations_tool_bar,
        }
        for key, value in self.tool_bars.items():
            value.addWidget(QtWidgets.QLabel(key))

    def set_mode(self):
        pass