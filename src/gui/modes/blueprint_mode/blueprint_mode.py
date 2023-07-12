
from src.gui.modes.mode_base import AbstractMode
from src.gui.modes.blueprint_mode.blueprint_view import BlueprintView
from src.gui.modes.blueprint_mode.blueprint_controls_widget import Ui_Form as BlueprintControlUI
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui, QtCore

class BlueprintMode(AbstractMode):
    def __init__(self, parent):
        super().__init__(parent=parent,
                        description="Blueprint Mode", 
                         icon_filename="mode-blueprint.ico", 
                         display=BlueprintView(), 
                         control_ui=BlueprintControlUI())
        
        self.blueprints_tool_bar = QtWidgets.QToolBar(parent=self.parent)
        self.blueprints_tool_bar.setFloatable(False)
        self.blueprints_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.blueprints_tool_bar.setHidden(False)
        self.parent.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.blueprints_tool_bar)
        
        
        self.tool_bars = {
            "Blueprints": self.blueprints_tool_bar,
        }
        for key, value in self.tool_bars.items():
            value.addWidget(QtWidgets.QLabel(key))

    def set_mode(self):
        pass