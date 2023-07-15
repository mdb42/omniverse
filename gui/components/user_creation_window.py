from gui.components.user_creation_widget import Ui_Form as UserCreationWidget
from src import utils
from local import constants
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from importlib.resources import files


class UserCreationWindow(QtWidgets.QWidget, UserCreationWidget):
    def __init__(self, parent=None):
        super(UserCreationWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(utils.load_icon("application-icon.ico")))
    
