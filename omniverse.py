import sys
from gui import omniverse_main
import keyring

from src import resource_utils, constants
from src.data.session_manager import SessionManager
from src.audio.audio_manager import AudioManager
from src.art.art_manager import ArtManager
from src.llms.llm_manager import LLMManager
from src.personas.persona_manager import PersonaManager
from langchain.callbacks.base import BaseCallbackManager
from gui.callbacks.streaming_browser_out import StreamingBrowserCallbackHandler

from gui.modes.presentation_mode.presentation_mode import PresentationMode
from gui.modes.canvas_mode.canvas_mode import CanvasMode, CanvasView
from gui.modes.blueprint_mode.blueprint_mode import BlueprintMode

from gui.components.chat_interface import ChatInterface

from gui.components.login_window import LoginWindow
from gui.components.user_creation_window import UserCreationWindow
from gui.components.workspace_creation_window import WorkspaceCreationWindow

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QToolBar, QHBoxLayout, QButtonGroup
from PyQt6.QtGui import QPixmap, QIcon, QTextCursor
from PyQt6.QtCore import QTimer, Qt


class Omniverse(QMainWindow, omniverse_main.Ui_MainWindow):
    """The Omniverse class that handles user interaction in the main window."""
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        self.setupUi(self)

        self.login_window = None
        self.user_creation_window = None
        self.workspace_creation_window = None

        self.session = SessionManager()
        
        if keyring.get_password(constants.TITLE, constants.WORKSPACE) is None:
            self.status_bar.showMessage("Omniverse workspace not in keyring. New workspace creation required.")
            self.workspace_creation_window = WorkspaceCreationWindow()
            self.workspace_creation_window.workspace_created_signal.connect(self.workspace_created)
            self.workspace_creation_window.closed_signal.connect(self.workspace_setup_window_closed)
            self.workspace_creation_window.show()
        
        # keyring.delete_password(constants.TITLE, constants.WORKSPACE) # Uncomment to reset workspace encryption key
        
        self.mode_index = 0 
        self.modes = [PresentationMode(parent=self), CanvasMode(parent=self), BlueprintMode(parent=self)]
        
        self.initialize_gui()

        if self.session.get_user_count() > 0 and keyring.get_password(constants.TITLE, constants.WORKSPACE) is not None:
            self.login_start()
        elif keyring.get_password(constants.TITLE, constants.WORKSPACE) is not None:
            self.create_new_user()

        # Initialize a QTimer for continuous constant advancement
        self.frame_timer = QTimer(self)
        self.frame_timer.timeout.connect(self.advance)
        self.frame_timer.start(int(1000/constants.FRAMES_PER_SECOND))

        # Still in design phase
        self.persona_manager = PersonaManager(session=self.session)

        # Setup the language model manager
        # TODO: Dynamically generate this from json data: currently at design phase in the new personas package
        self.browser_callbacks = {
            "response": BaseCallbackManager([StreamingBrowserCallbackHandler(self.chat_interface.chat_output_browser)]),
            "sentiment": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.sentiment_browser)]),
            "entity": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.entity_browser)]),
            "knowledge": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.knowledge_browser)]),
            "summary": BaseCallbackManager([StreamingBrowserCallbackHandler(self.modes[2].control_ui.summary_browser)])
        }

        self.llm_manager = LLMManager(session=self.session, 
                                      browser_callbacks=self.browser_callbacks, 
                                      assistant_id=constants.DEFAULT_PERSONA_NAME)
        self.current_user_prompt = ""
        self.current_generated_response = ""

        # Setup the AI art manager
        self.art_manager = ArtManager(session=self.session)
        self.current_generated_image = None

        # Setup the audio manager
        self.audio = AudioManager()
        # self.audio.play_sound_effect("click") # For testing

    def advance(self):
        """ Advance the application by one frame."""
        delta_time = self.frame_timer.interval() / 1000.0
        for mode in self.modes:
            mode.advance(delta_time)

    def preprocessing(self):
        """ Perform all preprocessing events, ending with the LLM preprocessor."""
        self.status_bar.showMessage("Grounding response...")
        self.modes[2].control_ui.sentiment_browser.clear()
        self.modes[2].control_ui.entity_browser.clear()
        QApplication.processEvents()
        self.llm_manager.preprocessing(self.current_user_prompt)
  
    def generate_response(self):
        """ Generate a response from the current user prompt."""
        self.status_bar.showMessage("Generating Response...")
        self.current_user_prompt = self.chat_interface.chat_input_text_editor.toPlainText().rstrip()
        self.chat_interface.chat_output_browser.append("\n" + str(self.session.current_user.name + ": " + self.current_user_prompt + "\n"))
        self.chat_interface.chat_input_text_editor.clear()
        self.chat_interface.chat_input_text_editor.setFocus()
        self.set_cursor_to_end(self.chat_interface.chat_output_browser)
        self.chat_interface.chat_output_browser.append(constants.DEFAULT_PERSONA_NAME + ": ")
        self.preprocessing()
        self.current_generated_response = self.llm_manager.generate_response()
        self.postprocessing()
        self.llm_manager.report_tokens()

    def postprocessing(self):
        """ Perform all postprocessing events, ending with the LLM postprocessor."""
        self.status_bar.showMessage("Reflecting on response...")
        if self.audio.text_to_speech:
            self.audio.play_text_to_speech(self.current_generated_response)
        QApplication.processEvents()
        self.llm_manager.postprocessing(self.current_user_prompt, self.current_generated_response)
        self.status_bar.showMessage("Response Complete.")
    
    def set_cursor_to_end(self, browser):
        """Set the cursor to the end of the browser, preventing the llm from overwriting the chat history."""
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()
    
    def generate_image(self):
        """ Generate an image from the current user prompt."""
        self.status_bar.showMessage("Generating Image...")
        prompt = self.chat_interface.chat_input_text_editor.toPlainText().rstrip()
        QApplication.processEvents()
        pixmap = QPixmap()
        pixmap.loadFromData(self.art_manager.generate_image(prompt))
        if not pixmap.isNull():
            self.current_generated_image = pixmap
            for mode in self.modes:
                if isinstance(mode.display, CanvasView):
                    mode.display.subject_pixmap = self.current_generated_image
            self.status_bar.showMessage("Image Generation Complete")
        else:
            self.status_bar.showMessage("Image Generation Failed")

    def toggle_text_to_speech(self):
        """ Toggle text to speech on and off."""
        self.status_bar.showMessage("Text to speech is now " + ("on." if not self.audio.text_to_speech else "off."))
        self.audio.text_to_speech = not self.audio.text_to_speech
        if self.audio.text_to_speech:
            self.chat_interface.tts_button.setIcon(QIcon(self.chat_interface.tts_on_button_icon_pixmap))
        else:
            self.chat_interface.tts_button.setIcon(QIcon(self.chat_interface.tts_off_button_icon_pixmap))

    def toggle_speech_to_text(self):
        """ Toggle speech to text on and off."""
        self.status_bar.showMessage("Speech to text is now " + ("on." if not self.audio.speech_to_text else "off."))
        self.audio.speech_to_text = not self.audio.speech_to_text
        if self.audio.speech_to_text:
            self.chat_interface.stt_button.setIcon(QIcon(self.chat_interface.stt_on_button_icon_pixmap))
        else:
            self.chat_interface.stt_button.setIcon(QIcon(self.chat_interface.stt_off_button_icon_pixmap))
    
    def set_mode(self):
        """ Set the current mode."""        
        self.mode_index = self.mode_selector_button_group.checkedId()
        self.displays_stacked_widget.setCurrentIndex(self.mode_index)
        self.controls_stacked_widget.setCurrentIndex(self.mode_index)
        for mode_index, mode in enumerate(self.modes):
            for tool_bar in mode.get_tool_bars():
                tool_bar.setVisible(mode_index == self.mode_index)
        self.status_bar.showMessage("Now in " + self.modes[self.mode_index].name + ".")

    def setup_window(self):
        """ Setup the main window."""
        self.setWindowTitle(f"{constants.TITLE} {constants.VERSION}")
        self.setWindowIcon(QIcon(resource_utils.load_icon("application-icon.ico")))
        self.main_splitter.setSizes([int(self.width() * 0.20), int(self.width() * 0.50), int(self.width() * 0.30)])
        self.status_bar.showMessage("Welcome to the Omniverse!")

    def create_mode_selector_tool_bar(self):
        """ Create the mode selector tool bar."""
        self.mode_selector_tool_bar = QToolBar(self)
        self.mode_selector_tool_bar.setMovable(False)
        self.mode_selector_tool_bar.setFloatable(False)
        self.mode_selector_tool_bar.setOrientation(Qt.Orientation.Horizontal)
        self.mode_selector_tool_bar.setHidden(False)
        self.mode_selector_tool_bar.setContentsMargins(2,2,2,2)
        self.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.mode_selector_tool_bar)
        self.mode_selector_tool_bar.setFixedHeight(40)

    def add_modes(self):
        """ Add the modes to the application."""
        self.mode_selection_widget = QWidget()
        self.mode_selection_layout = QHBoxLayout()
        self.mode_selection_widget.setLayout(self.mode_selection_layout)
        self.mode_selection_layout.setContentsMargins(2,2,2,2)
        self.mode_selector_button_group = QButtonGroup()
        self.mode_selector_button_group.setExclusive(True)
        self.mode_selector_button_group.buttonClicked.connect(self.set_mode) 
        self.mode_selector_tool_bar.addWidget(self.mode_selection_widget)

        for mode_index, mode in enumerate(self.modes):
            for tool_bar in mode.get_tool_bars():
                self.addToolBar(Qt.ToolBarArea.TopToolBarArea, tool_bar)

            mode_button = mode.button
            mode_button.setCheckable(True)
            mode_button.setAutoExclusive(True)
            self.mode_selector_button_group.addButton(mode_button, mode_index)
            self.mode_selection_layout.addWidget(mode_button)
            self.mode_selector_tool_bar.addWidget(mode_button)
            if mode_index == self.mode_index:
                mode_button.setChecked(True)  

            self.displays_stacked_widget.addWidget(mode.display)
            self.controls_stacked_widget.addWidget(mode.control_widget)

    def login_successful(self):
        """ Perform actions after a successful login."""
        self.status_bar.showMessage(f"Logged in as {self.session.current_user.name}.")
        self.session.setup()
        self.llm_manager.setup()
        if not self.isActiveWindow():
            self.activateWindow()
        self.raise_()
    
    def login_start(self):
        """ Start the login process."""
        self.status_bar.showMessage("Login to start session.")
        self.login_window = LoginWindow(session=self.session)
        self.login_window.closed_signal.connect(self.login_window_closed)
        self.login_window.login_succeeded_signal.connect(self.login_successful)
        self.login_window.create_new_user_clicked_signal.connect(self.create_new_user)
        self.login_window.show()

    def new_user_created(self):
        """ Perform actions after a new user is created."""
        self.status_bar.showMessage(f"New user created: {self.session.get_most_recent_user().name}.")
        self.user_creation_window.hide()
        self.login_start()
        if not self.isActiveWindow():
            self.activateWindow()
        self.raise_()
        
    def create_new_user(self):
        self.status_bar.showMessage("Creating a new user.")
        """ Create a new user."""
        if self.login_window is not None: self.login_window.hide()
        # User Creation Window
        self.user_creation_window = UserCreationWindow(session=self.session)
        self.user_creation_window.user_created_signal.connect(self.new_user_created)
        self.user_creation_window.window_closed_signal.connect(self.user_creation_window_closed)
        self.user_creation_window.show()

    def on_exit(self):
        """ Close the application. """
        self.status_bar.showMessage("Exiting the Omniverse...")
        self.session.close()
        self.close()
    
    def workspace_setup_window_closed(self):
        """ Perform actions after the workspace setup is closed."""
        if keyring.get_password(constants.TITLE, constants.WORKSPACE):
            self.close()
    
    def login_window_closed(self):
        """ Perform actions after the login is closed."""
        if self.session.current_user is None:
            self.close()

    def user_creation_window_closed(self):
        """ Perform actions after the user creation is closed."""
        if self.session.get_user_count() == 0:
            self.close()
        else:
            self.login_start()

    def workspace_created(self):
        """ Perform actions after a new workspace is created."""
        self.status_bar.showMessage("New workspace created.")
        key = self.workspace_creation_window.get_key()
        self.login_window = LoginWindow(session=self.session) # Reset the login window
        self.workspace_creation_window.close()
        if key is not None and key != "":
            keyring.set_password(constants.TITLE, constants.WORKSPACE, key)
            if self.session.get_user_count() == 0:
                self.create_new_user()
            else:
                self.login_start()

    def initialize_gui(self):
        """ Initialize the GUI. """
        self.setup_window()
        self.create_mode_selector_tool_bar()
        self.add_modes()
        self.set_mode()
        self.show()

        # Chat interface widget
        self.chat_interface_widget = QWidget()
        self.chat_interface = ChatInterface(self.chat_interface_widget)
        self.chat_stacked_widget.addWidget(self.chat_interface_widget)        
        self.chat_interface.tts_button.clicked.connect(self.toggle_text_to_speech)
        self.chat_interface.stt_button.clicked.connect(self.toggle_speech_to_text)
        self.chat_interface.generate_text_button.clicked.connect(self.generate_response)
        self.chat_interface.generate_image_button.clicked.connect(self.generate_image)
       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Omniverse()
    app.aboutToQuit.connect(window.on_exit)
    sys.exit(app.exec())


    