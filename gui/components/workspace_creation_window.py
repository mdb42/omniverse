from gui.components.workspace_creation_widget import Ui_Form as WorkspaceCreationWidget
from src import resource_utils, constants
import keyring

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtCore import Qt, pyqtSignal, QSize
from PyQt6.QtGui import QIcon
import base64
import os

class WorkspaceCreationWindow(QWidget, WorkspaceCreationWidget):
    workspace_created_signal = pyqtSignal(bool)
    closed_signal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(WorkspaceCreationWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(resource_utils.load_icon("application-icon.ico")))
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)
        self.setFixedSize(self.size())
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        self.copy_to_clipboard_button.setIcon(QIcon(resource_utils.load_icon("clipboard-icon.ico")))
        self.random_key_button.setIcon(QIcon(resource_utils.load_icon("refresh-icon.ico")))
        self.visibility_on_icon = QIcon(resource_utils.load_icon("visibility-on-icon.ico"))        
        self.visibility_off_icon = QIcon(resource_utils.load_icon("visibility-off-icon.ico"))
        self.echo_toggle_button.setIcon(self.visibility_off_icon)
        self.continue_button.clicked.connect(self.continue_button_clicked)
        self.random_key_button.clicked.connect(self.random_key_button_clicked)
        self.copy_to_clipboard_button.clicked.connect(self.copy_to_clipboard_button_clicked)
        self.echo_toggle_button.clicked.connect(self.echo_toggle_button_clicked)
        self.key_line_edit.textChanged.connect(self.key_line_edit_changed)
        self.key_line_edit_changed()

    def random_key_button_clicked(self):
        self.key_line_edit.setText(self.generate_random_key())
    
    def generate_random_key(self):
        key_bytes = os.urandom(32)
        key_b64_string = base64.urlsafe_b64encode(key_bytes).decode('utf-8')
        return key_b64_string
    
    def key_line_edit_changed(self):
        if len(self.key_line_edit.text()) != 44:
            self.continue_button.setEnabled(False)
        else:
            self.continue_button.setEnabled(True)

        if len(self.key_line_edit.text()) > 44:
            self.key_line_edit.setText(self.key_line_edit.text()[:44])

    def copy_to_clipboard_button_clicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.key_line_edit.text())

    def echo_toggle_button_clicked(self):
        if self.echo_toggle_button.isChecked():
            self.echo_toggle_button.setIcon(self.visibility_on_icon)
            self.echo_toggle_button.setIconSize(QSize(16, 15))
            self.key_line_edit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.echo_toggle_button.setIcon(self.visibility_off_icon)
            self.echo_toggle_button.setIconSize(QSize(16, 16))
            self.key_line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def closeEvent(self, event):
        self.closed_signal.emit(True)
        event.accept()

    def continue_button_clicked(self):
        self.workspace_created_signal.emit(True)

    def get_key(self):
        if len(self.key_line_edit.text()) == 44:
            return self.key_line_edit.text()
        else:
            return None
    
    def closeEvent(self, event):
        """Reimplemented from QWidget class to handle the close event in the login window."""
        if keyring.get_password(constants.TITLE, constants.WORKSPACE) is None:
            self.closed_signal.emit(True)
        event.accept()
    
        
    
        





        



    
