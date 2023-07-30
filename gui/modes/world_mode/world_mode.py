from gui.modes.mode_base import ModeBase
from gui.modes.world_mode.world_view import WorldView
from gui.modes.world_mode.world_controls_widget import Ui_Form as WorldControlUI
from PyQt6.QtCore import Qt
from PyQt6 import QtWidgets

class WorldMode(ModeBase):
    def __init__(self, parent):
        super().__init__(parent=parent,
                         name = "World Mode",
                        description="Default view for presenting world simulations", 
                         icon_filename="world-icon.ico", 
                         display=WorldView(), 
                         control_ui=WorldControlUI())        
        
        self.worlds_tool_bar = QtWidgets.QToolBar(parent=self.parent)
        self.worlds_tool_bar.setFloatable(False)
        self.worlds_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.worlds_tool_bar.setHidden(False)
        self.parent.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.worlds_tool_bar)
        
        self.tool_bars = {
            "Worlds": self.worlds_tool_bar,
        }
        for key, value in self.tool_bars.items():
            value.addWidget(QtWidgets.QLabel(key))

    def set_mode(self):
        pass

    def generate_tool_bars(self):
        return {}