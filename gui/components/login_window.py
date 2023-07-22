from gui.components.login_widget import Ui_Form as LoginWidget
from src import resource_utils
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore
import webbrowser
from importlib.resources import files
import src.data.data_utils as data_utils

GITHUB_URL = "https://github.com/mdb42/omniverse/tree/main"
CREATOR_TWITTER_URL = "https://twitter.com/mdelbranson"
DISCORD_URL = "https://discord.gg/98Qub3gdnY"



class LoginWindow(QtWidgets.QWidget, LoginWidget):
    """The LoginWindow class that handles user interaction in the login form."""

    login_successful_signal = QtCore.pyqtSignal(bool)
    incorrect_password_signal = QtCore.pyqtSignal(bool)
    create_new_user_signal = QtCore.pyqtSignal(bool)
    window_closed_signal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None, session=None):
        """Initializes the login window, sets up the UI, and connects the signal and slots."""
        super(LoginWindow, self).__init__(parent)
        self.session = session
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(resource_utils.load_icon("application-icon.ico")))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setFixedSize(self.size())
        self.setWindowTitle("Login")
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.twitter_button.setIcon(QIcon(resource_utils.load_icon("twitter-icon.ico")))
        self.discord_button.setIcon(QIcon(resource_utils.load_icon("discord-icon.ico")))
        self.github_button.setIcon(QIcon(resource_utils.load_icon("github-icon.ico")))
        self.github_button.clicked.connect(self.github_button_clicked)
        self.discord_button.clicked.connect(self.discord_button_clicked)
        self.twitter_button.clicked.connect(self.twitter_button_clicked)
        self.create_new_user_button.clicked.connect(self.create_new_user_button_clicked)

        self.setup_combo_box()
        self.login_button.clicked.connect(self.login_button_clicked)

        self.password_line_edit.textChanged.connect(self.password_line_edit_changed)
        self.password_line_edit_changed()

    def setup_combo_box(self):
        self.name_combo_box.clear()
        if self.session is not None and self.session.users_session is not None:
            for name in self.session.get_all_user_names_by_last_login():
                self.name_combo_box.addItem(name)        
            self.name_combo_box.currentTextChanged.connect(self.name_combo_box_changed)
            self.name_combo_box_changed()

    def name_combo_box_changed(self):
        """Slot for handling the event when the selected user in the combo box changes."""
        name = self.name_combo_box.currentText()
        user = self.session.get_user_by_name(name)
        if user: 
            decrypted_remembered_status = data_utils.decrypt(user.remember_me)
            print("Remembered Status: " + str(decrypted_remembered_status))
            if decrypted_remembered_status == True:
                self.password_line_edit.setText("**********")
                self.remember_me_checkbox.setChecked(True)
            else:
                self.password_line_edit.setText("")
                self.remember_me_checkbox.setChecked(False)

    def login_button_clicked(self):
        """Slot for handling the event when the login button is clicked. It performs
            the login process and emits appropriate signals."""
        print("Login Button Clicked")
        username = self.name_combo_box.currentText()
        password = self.password_line_edit.text()
        remember_me = self.remember_me_checkbox.isChecked()
        if self.session.login_user(username, password, remember_me):
            print("Login Successful")
            self.login_successful_signal.emit(True)
            self.close()
        else:
            print("Login Failed")
            self.feedback_label.setText("Incorrect Password")
            self.feedback_label.setStyleSheet("color: red")
            self.password_line_edit.setText("")
            self.password_line_edit.setFocus()
            self.incorrect_password_signal.emit(True)

    def create_new_user_button_clicked(self):
        """Slot for handling the event when the create new user button is clicked. It
            opens the new user creation window and closes the login window."""
        print("Create New User Button Clicked")
        self.create_new_user_signal.emit(True)
        
    
    def password_line_edit_changed(self):
        """Slot for handling the event when the text in the password line edit changes. 
           It enables or disables the login button based on whether the password field is empty."""
        if self.password_line_edit.text() == "":
            self.login_button.setEnabled(False)
        else:
            self.login_button.setEnabled(True)
    
    def keyPressEvent(self, event):
        """Reimplemented from QWidget class to handle the key press events in the login window."""
        if event.key() == Qt.Key.Key_Return and self.password_line_edit.hasFocus():
            self.login_button_clicked()
        else:
            super().keyPressEvent(event)

    def twitter_button_clicked(self):
        """Slot for handling the event when the Twitter button is clicked. 
           It opens the Twitter URL in the default web browser."""
        webbrowser.open(CREATOR_TWITTER_URL)
    
    def discord_button_clicked(self):
        """Slot for handling the event when the Discord button is clicked. 
           It opens the Discord URL in the default web browser."""
        webbrowser.open(DISCORD_URL)
    
    def github_button_clicked(self):
        """Slot for handling the event when the Github button is clicked. 
           It opens the Github URL in the default web browser."""
        webbrowser.open(GITHUB_URL)
    
    def closeEvent(self, event):
        """Reimplemented from QWidget class to handle the close event in the login window."""
        if self.session.current_user is None:
            self.window_closed_signal.emit(True)
        event.accept()
    

