import os
from abc import ABC, abstractmethod
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QHBoxLayout, QGridLayout, QToolButton, QPushButton, QWidget
from src import resource_utils

class ModeBase(ABC):
    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get('parent', None)
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', "")
        self.display = kwargs.get('display', None)

        # Every mode will have a button to activate it
        self.icon_filename = kwargs.get('icon_filename', "application-icon.ico")
        self.icon_pixmap = resource_utils.load_icon(self.icon_filename)
        self.button = QtWidgets.QPushButton()
        self.button.setCheckable(True)
        self.button.setIcon(QtGui.QIcon(self.icon_pixmap))
        self.button.setToolTip(self.name)
        self.button.setFixedSize(32, 32)
        
        # Every mode will have a display widget, to accept whatever display type is passed in
        self.display_widget = QtWidgets.QWidget()
        self.display_layout = QtWidgets.QGridLayout()
        self.display_layout.setContentsMargins(0, 0, 0, 0)
        self.display_layout.setSpacing(0)
        self.display_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display_widget.setLayout(self.display_layout)
        self.display_layout.addWidget(self.display)
        
        # Every mode will have a control widget, to accept whatever interface is passed in
        self.control_ui = kwargs.get('control_ui', None)
        self.control_widget = QtWidgets.QWidget()        
        self.control_ui.setupUi(self.control_widget)
        self.control_widget.setContentsMargins(0, 0, 0, 0)

        # Every mode will have a dictionary of toolbars, which each mode can define however they like
        self.tool_bars = self.generate_tool_bars()

    def get_tool_bars(self):
        # Return just a list of the values
        return self.tool_bars.values()
    
    def advance(self, delta_time):
        if hasattr(self.display, 'advance'):
            self.display.advance(delta_time)
 
    @abstractmethod
    def set_mode(self):
        pass

    @abstractmethod
    def generate_tool_bars(self):
        pass


    

    
