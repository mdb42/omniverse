from gui.components.login_widget import Ui_Form as LoginWidget
from gui.components.user_creation_window import UserCreationWindow
from src import utils
from local import constants
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QImage, QPixmap
import webbrowser
from importlib.resources import files


class LoginWindow(QtWidgets.QWidget, LoginWidget):
    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowIcon(QIcon(utils.load_icon("application-icon.ico")))
        
        self.twitter_button.setIcon(QIcon(utils.load_icon("twitter-icon.ico")))
        self.discord_button.setIcon(QIcon(utils.load_icon("discord-icon.ico")))
        self.github_button.setIcon(QIcon(utils.load_icon("github-icon.ico")))
        self.github_button.clicked.connect(self.github_button_clicked)
        self.discord_button.clicked.connect(self.discord_button_clicked)
        self.twitter_button.clicked.connect(self.twitter_button_clicked)
        self.create_new_user_button.clicked.connect(self.create_new_user_button_clicked)

        
    def twitter_button_clicked(self):
        webbrowser.open(constants.CREATOR_TWITTER_URL)
    
    def discord_button_clicked(self):
        webbrowser.open(constants.DISCORD_URL)
    
    def github_button_clicked(self):
        webbrowser.open(constants.GITHUB_URL)

    def create_new_user_button_clicked(self):
        print("Create New User Clicked")
        self.user_creation_window = UserCreationWindow()
        self.user_creation_window.show()        
        self.close()
