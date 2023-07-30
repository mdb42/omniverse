import os
from abc import ABC, abstractmethod
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton
from gui import gui_utils


class ActionBase(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()
        """ Base class for mode specific buttons in the toolbar."""
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', self.name)
        self.tool_tip = kwargs.get('tool_tip', self.description)
        self.icon_filename = kwargs.get('icon_filename', "application-icon.ico")
        self.icon = gui_utils.load_icon(self.icon_filename)
        self.handler = kwargs.get('handler', None)
        self.enabled_signal = kwargs.get('enabled_signal', None)
        self.button = self.load_button()

    def load_button(self):
        self.button = QPushButton()
        self.button.setIcon(QIcon(gui_utils.load_icon(self.icon_filename)))
        self.button.setToolTip(self.tool_tip)
        self.button.setFixedSize(32, 32)
        self.button.setContentsMargins(2, 2, 2, 2)
        if self.handler: self.button.clicked.connect(self.handler)
        if self.enabled_signal: self.enabled_signal.connect(self.button.setEnabled)
        return self.button
    
    
        
