from gui.components.developer_widget import Ui_Form as DeveloperWidget
from gui import gui_utils
from src import constants

from PyQt6.QtWidgets import QWidget, QTextBrowser
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QIcon
import webbrowser
import src.data.data_utils as data_utils
from src.logger_utils import create_logger


class DeveloperWindow(QWidget, DeveloperWidget):
    """The Developer Window holds widgets for developer use."""

    def __init__(self, parent=None):
        """Initializes the login window, sets up the UI, and connects the signal and slots."""
        super(DeveloperWindow, self).__init__(parent)
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("Initializing Developer Window")       
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(gui_utils.load_icon("application-icon.ico")))
        self.setWindowTitle("Developer Window")

    def onClosed(self):
        self.logger.info("Developer Window: Hiding")
        self.hide()

    def clear(self):
        self.logger.info("Developer Window: Clearing")
        # let's recursively iterate through all the widgets in the window
        # and if they are a QTextBrowser, we will clear the text
        for child in self.findChildren(QWidget):
            if isinstance(child, QTextBrowser):
                child.clear()

    