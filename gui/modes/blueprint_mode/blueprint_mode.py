
from gui.modes.mode_base import ModeBase
from gui.modes.blueprint_mode.blueprint_view import BlueprintView
from gui.modes.blueprint_mode.blueprint_controls_widget import Ui_Form as BlueprintControlUI
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets, QtGui, QtCore

class BlueprintMode(ModeBase):
    def __init__(self, parent):
        super().__init__(parent=parent,
                         name = "Blueprint Mode",
                        description="Visual programming interface for language model prompt grounding", 
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

    def generate_tool_bars(self):
        return {}