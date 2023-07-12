import os
from abc import ABC, abstractmethod
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage, QIcon, QCursor
from importlib.resources import files
from PyQt6.QtWidgets import QHBoxLayout
# Let's import QBushButton
from PyQt6.QtWidgets import QPushButton


class ToolBase(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__()
        """ Base class for mode specific buttons in the toolbar."""
        self.name = kwargs.get('name', "")
        self.description = kwargs.get('description', self.name)
        self.tooltip = kwargs.get('tooltip', self.description)
        self.icon_filename = kwargs.get('icon_filename', "application-icon.ico")
        self.icon = self.load_icon(self.icon_filename)
        self.handler = kwargs.get('handler', None)
        self.button = self.load_button()
  
    def load_icon(self, resource):
        resource_path = files("resources.icons") / resource
        with open(resource_path, 'rb') as file:
            icon_data = file.read()
        icon_image = QImage.fromData(icon_data)
        return QPixmap.fromImage(icon_image)
    
    def load_button(self):
        self.button = QPushButton()
        self.button.setIcon(QIcon(self.load_icon(self.icon_filename)))
        self.button.setToolTip(self.tooltip)
        # self.button.clicked.connect(self.handler)
        return self.button
    
    
        
