import sys, os
from local import constants
from src.gui import omniverse_window
from src.gui.windows.login_window import Ui_Form as LoginUI
from src.gui.windows.user_creation_window import Ui_Form as UserCreationUI
from src.gui.components.tool_bar_widget import Ui_Form as ToolBarUI
from src.gui.components.canvas_mode_tool_widget import Ui_Form as CanvasModeToolUI

from importlib.resources import files
from src.data.session_manager import SessionManager
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMenu
from PyQt6.QtGui import QPixmap, QIcon, QImage, QTextCursor
from PyQt6.QtCore import QTimer, Qt, QPoint

from src.audio.audio_manager import AudioManager
from src.art.art_manager import ArtManager

from src.llms.llm_manager import LLMManager
from langchain.callbacks.base import BaseCallbackManager

import webbrowser

from src.gui.callbacks.streaming_browser_out import StreamingBrowserCallbackHandler

from src.gui.presentation_view.presentation_view import PresentationView
from src.gui.canvas_view.canvas_view import CanvasView
from src.gui.blueprint_view.blueprint_view import BlueprintView

from enum import Enum

TITLE = "Omniverse"
VERSION = "0.0.4"
FRAMES_PER_SECOND = 66

class Mode(Enum):
    PRESENTATION = (0, "Presentation Mode", "mode-present.ico")
    CANVAS = (1, "Canvas Mode", "mode-canvas.ico")
    BLUEPRINT = (2, "Blueprint Mode", "mode-blueprint.ico")

class Omniverse(QtWidgets.QMainWindow, omniverse_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        self.setupUi(self)  
        self.initialize_gui()
        self.mode = Mode.PRESENTATION 
        self.session = SessionManager(app_name=TITLE, key=constants.DEFAULT_ENCRYPTION_KEY)

        # Initialize a QTimer for continuous constant advancement
        self.frame_timer = QTimer(self)
        self.frame_timer.timeout.connect(self.advance)
        self.frame_timer.start(int(1000/FRAMES_PER_SECOND))

        # Setup the language model manager
        # These callbacks are only for the prototype implementation
        # TODO: Remove these callbacks and replace with a json file defining completion batch sequences
        # TODO: Dynamically generate necessary widgets to display the completion types as required
        self.assistant_id = constants.DEFAULT_AI_NAME
        self.browser_callbacks = {
            "response": BaseCallbackManager([StreamingBrowserCallbackHandler(self.response_text_browser)]),
            "sentiment": BaseCallbackManager([StreamingBrowserCallbackHandler(self.sentiment_browser)]),
            "entity": BaseCallbackManager([StreamingBrowserCallbackHandler(self.entity_browser)]),
            "knowledge": BaseCallbackManager([StreamingBrowserCallbackHandler(self.knowledge_browser)]),
            "summary": BaseCallbackManager([StreamingBrowserCallbackHandler(self.summary_browser)])
        }

        self.llm_manager = LLMManager(self.browser_callbacks, "Matthew", self.assistant_id)
        self.current_user_prompt = ""
        self.current_generated_response = ""

        # Setup the AI art manager
        self.art_manager = ArtManager()
        self.current_generated_image = None

        # Setup the audio manager
        self.audio = AudioManager()
        self.audio.play_sound_effect("click") # For testing   

        print(self.width(), self.height())
        
        

    def advance(self):
        delta_time = self.frame_timer.interval() / 1000.0
        self.canvas_view.advance(delta_time)
        self.blueprint_view.advance(delta_time)
  
    def generate_response(self):
        self.current_user_prompt = self.input_text_editor.toPlainText().rstrip()
        self.response_text_browser.append("\n" + str(self.session.current_user_name + ": " + self.current_user_prompt + "\n"))
        self.input_text_editor.clear()
        self.input_text_editor.setFocus()
        """ Generate a response from the LLM Manager."""
        print("Generating Response")
        self.set_cursor_to_end(self.response_text_browser)
        self.response_text_browser.append(self.assistant_id + ": ")
        self.preprocessing()
        self.current_generated_response = self.llm_manager.generate_response()
        self.postprocessing()
        self.llm_manager.report_tokens()

    def preprocessing(self):
        """ Perform all preprocessing events, ending with the LLM preprocessor."""
        print("Preprocessing Prompt Grounding")
        self.sentiment_browser.clear()
        self.entity_browser.clear()
        QtWidgets.QApplication.processEvents()
        self.llm_manager.preprocessing(self.current_user_prompt)

    def postprocessing(self):
        """ Perform all postprocessing events, ending with the LLM postprocessor."""
        print("Postprocessing Model Output")
        if self.audio.text_to_speech:
            self.audio.play_text_to_speech(self.current_generated_response)

        self.summary_browser.clear()
        self.knowledge_browser.clear()
        QtWidgets.QApplication.processEvents()
        print("Going to LLM Manager Post Processing")
        self.llm_manager.postprocessing(self.current_user_prompt, self.current_generated_response)
        print("Finished LLM Manager Post Processing")
    
    def set_cursor_to_end(self, browser):
        # Set the cursor to the end of the browser, preventing the llm from overwriting the chat history
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()
    
    def generate_image(self):
        prompt = self.input_text_editor.toPlainText().rstrip()
        QtWidgets.QApplication.processEvents()
        pixmap = QPixmap()
        pixmap.loadFromData(self.art_manager.generate_image(prompt))
        if not pixmap.isNull():
            self.current_generated_image = pixmap
            self.canvas_view.subject_pixmap = self.current_generated_image
        else:
            print("Image generation failed.")

    def toggle_text_to_speech(self):
        self.audio.text_to_speech = not self.audio.text_to_speech
        if self.audio.text_to_speech:
            self.tts_mode_button.setIcon(QIcon(self.tts_on_button_icon_pixmap))
        else:
            self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

    def toggle_speech_to_text(self):
        self.audio.speech_to_text = not self.audio.speech_to_text
        if self.audio.speech_to_text:
            self.stt_mode_button.setIcon(QIcon(self.stt_on_button_icon_pixmap))
        else:
            self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))

    def login_button_clicked(self):
        print("Logging in")

    def twitter_button_clicked(self):
        webbrowser.open(constants.CREATOR_TWITTER_URL)
    
    def discord_button_clicked(self):
        webbrowser.open(constants.DISCORD_URL)
    
    def github_button_clicked(self):
        webbrowser.open(constants.GITHUB_URL)

        

    def create_new_user_button_clicked(self):
        print("Create New User Clicked")
        self.exit_login()
        self.user_creation_widget.show()
    
    def exit_login(self):
        self.login_widget.close()

    def set_mode(self):
        index = self.mode_button_group.checkedId()
        self.mode = next((m for m in Mode if m.value[0] == index), None)
        self.central_stacked_widget.setCurrentIndex(self.mode.value[0])
        self.control_stacked_widget.setCurrentIndex(self.mode.value[0])  
        self.mode_tools_stacked_widget.setCurrentIndex(self.mode.value[0])

    def load_icon(self, resource):
        resource_path = files("resources.icons") / resource
        with open(resource_path, 'rb') as file:
            icon_data = file.read()
        icon_image = QImage.fromData(icon_data)
        return QPixmap.fromImage(icon_image)
    
    def initialize_gui(self):
        """ Initialize the GUI. """
        # Setup the application window
        self.setWindowTitle(f"{TITLE} {VERSION}")
        self.application_icon_pixmap = self.load_icon("application-icon.ico")
        self.setWindowIcon(QIcon(self.application_icon_pixmap))

        
        dock_width = self.width() // 6  
        self.chat_dock_widget.setMinimumWidth(dock_width)

        # Add the presentation view to the presentation view widget
        self.presentation_view = PresentationView(parent=self)
        self.presentation_view_widget.layout().addWidget(self.presentation_view)
        
        # Add the canvas view to the canvas view widget
        self.canvas_view = CanvasView(parent=self)
        self.canvas_view_widget.layout().addWidget(self.canvas_view)

        # The blueprint widget has other widgets inside of it, so we need to add it to the top of its vertical widget
        self.blueprint_view = BlueprintView(parent=self)
        self.blueprint_view_vertical_widget.layout().insertWidget(0, self.blueprint_view)
        self.blueprint_view_vertical_widget.layout().setStretch(1, 1)
        self.blueprint_view_vertical_widget.layout().setStretchFactor(self.blueprint_view, 1)

        self.tool_bar_layout = QtWidgets.QHBoxLayout()
        self.tool_bar_layout.setContentsMargins(2, 2, 2, 2)
        self.tool_bar_layout.setSpacing(0)

        self.mode_button_group = QtWidgets.QButtonGroup()
        self.mode_button_group.buttonClicked.connect(self.set_mode)
        self.mode_button_group_widget = QtWidgets.QWidget()
        self.mode_button_group_layout = QtWidgets.QHBoxLayout()
        self.mode_button_group_layout.setSpacing(2)
        self.mode_button_group_layout.setContentsMargins(2, 2, 2, 2)
        
        self.mode_tools_stacked_widget = QtWidgets.QStackedWidget()
        self.mode_tools_stacked_widget.setContentsMargins(2, 2, 2, 2)    

        self.canvas_mode_tools_widget = QtWidgets.QWidget()
        self.canvas_mode_tools_ui = CanvasModeToolUI()
        self.canvas_mode_tools_ui.setupUi(self.canvas_mode_tools_widget)
        self.canvas_mode_tools_ui.fill_color_button.set_color(self.canvas_view.fill_color)
        self.canvas_mode_tools_ui.stroke_color_button.set_color(self.canvas_view.stroke_color)

        for mode in Mode:
            mode_button = QtWidgets.QPushButton()
            mode_button.setToolTip(mode.value[1])
            mode_button.setIcon(QIcon(self.load_icon(mode.value[2])))
            mode_button.setFixedSize(32, 32)
            mode_button.setCheckable(True)
            if mode == Mode.PRESENTATION:
                mode_button.setChecked(True)
            self.mode_button_group.addButton(mode_button)
            self.mode_button_group.setId(mode_button, mode.value[0])
            self.mode_button_group_layout.addWidget(mode_button)
            mode_tools_widget = QtWidgets.QWidget()
            mode_tools_layout = QtWidgets.QHBoxLayout()
            mode_tools_layout.setContentsMargins(2, 2, 2, 2)
            mode_tools_layout.setSpacing(0)
            mode_tools_widget.setLayout(mode_tools_layout)
            # Adding a placeholder label for now, unless it's canvas mode
            if mode == Mode.CANVAS:
                mode_tools_layout.addWidget(self.canvas_mode_tools_widget)
            else:
                mode_tools_label = QtWidgets.QLabel()
                mode_tools_label.setText(mode.value[1])
                mode_tools_layout.addWidget(mode_tools_label)
            self.mode_tools_stacked_widget.addWidget(mode_tools_widget)
        self.mode_button_group_widget.setLayout(self.mode_button_group_layout)
        self.tool_bar_layout.addWidget(self.mode_button_group_widget)
        self.tool_bar_layout.addWidget(self.mode_tools_stacked_widget)
        self.tool_bar.addWidget(self.mode_button_group_widget)
        self.tool_bar.addWidget(self.mode_tools_stacked_widget)        
        # let's add a horizontal spacer to the right of the tool bar
        # let's adjust Expanding and Minimum for PyQt6
        horizontal_spacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.tool_bar_layout.addItem(horizontal_spacer)



        # Other Windows
        self.login_widget = QtWidgets.QWidget()
        self.login_ui = LoginUI()
        self.login_ui.setupUi(self.login_widget)
        self.login_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.login_widget.setWindowIcon(QIcon(self.application_icon_pixmap))
        self.login_widget.show()

        self.user_creation_widget = QtWidgets.QWidget()
        self.user_creation_ui = UserCreationUI()
        self.user_creation_ui.setupUi(self.user_creation_widget)
        self.user_creation_widget.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.user_creation_widget.setWindowIcon(QIcon(self.application_icon_pixmap))

        # Setup the dynamic components
        self.tts_on_button_icon_pixmap = self.load_icon("button-tts-on.ico")
        self.tts_off_button_icon_pixmap = self.load_icon("button-tts-off.ico")
        self.stt_on_button_icon_pixmap = self.load_icon("button-stt-on.ico")
        self.stt_off_button_icon_pixmap = self.load_icon("button-stt-off.ico")

        # Set the starting icons for the dynamic components
        self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))
        self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
        
        # Setup static components
        self.generate_text_button.setIcon(QIcon(self.load_icon("button-generate-text.ico")))
        self.generate_image_button.setIcon(QIcon(self.load_icon("button-generate-image.ico")))

        # Setup static toolbar components
        self.canvas_mode_tools_ui.pencil_button.setIcon(QIcon(self.load_icon("tool-pencil.ico")))
        self.canvas_mode_tools_ui.erase_button.setIcon(QIcon(self.load_icon("tool-eraser.ico")))
        self.canvas_mode_tools_ui.line_button.setIcon(QIcon(self.load_icon("tool-line.ico")))
        self.canvas_mode_tools_ui.ellipse_button.setIcon(QIcon(self.load_icon("tool-circle.ico")))
        self.canvas_mode_tools_ui.rectangle_button.setIcon(QIcon(self.load_icon("tool-square.ico")))
        self.canvas_mode_tools_ui.undo_button.setIcon(QIcon(self.load_icon("button-undo.ico")))
        self.canvas_mode_tools_ui.redo_button.setIcon(QIcon(self.load_icon("button-redo.ico")))
        self.canvas_mode_tools_ui.new_button.setIcon(QIcon(self.load_icon("button-new.ico")))
        self.canvas_mode_tools_ui.open_button.setIcon(QIcon(self.load_icon("button-open.ico")))
        self.canvas_mode_tools_ui.save_button.setIcon(QIcon(self.load_icon("button-save.ico")))
        self.canvas_mode_tools_ui.image_button.setIcon(QIcon(self.load_icon("tool-image.ico")))

        # Setup static login widget components
        self.login_ui.twitter_button.setIcon(QIcon(self.load_icon("twitter-icon.ico")))
        self.login_ui.discord_button.setIcon(QIcon(self.load_icon("discord-icon.ico")))
        self.login_ui.github_button.setIcon(QIcon(self.load_icon("github-icon.ico")))

        # Connect signals to methods
        self.canvas_view.undoAvailable.connect(self.canvas_mode_tools_ui.undo_button.setEnabled)
        self.canvas_view.redoAvailable.connect(self.canvas_mode_tools_ui.redo_button.setEnabled)

        self.tts_mode_button.clicked.connect(self.toggle_text_to_speech)
        self.stt_mode_button.clicked.connect(self.toggle_speech_to_text)
        self.generate_text_button.clicked.connect(self.generate_response)
        self.generate_image_button.clicked.connect(self.generate_image)

        self.canvas_mode_tools_ui.pencil_button.clicked.connect(self.canvas_view.set_pencil_tool)
        self.canvas_mode_tools_ui.erase_button.clicked.connect(self.canvas_view.set_erase_tool)
        self.canvas_mode_tools_ui.line_button.clicked.connect(self.canvas_view.set_line_tool)
        self.canvas_mode_tools_ui.ellipse_button.clicked.connect(self.canvas_view.set_ellipse_tool)
        self.canvas_mode_tools_ui.rectangle_button.clicked.connect(self.canvas_view.set_rectangle_tool)
        self.canvas_mode_tools_ui.undo_button.clicked.connect(self.canvas_view.undo)
        self.canvas_mode_tools_ui.redo_button.clicked.connect(self.canvas_view.redo)
        self.canvas_mode_tools_ui.new_button.clicked.connect(self.canvas_view.clear)
        self.canvas_mode_tools_ui.stroke_color_button.color_changed.connect(self.canvas_view.set_tool_color)        
        self.canvas_mode_tools_ui.stroke_width_spin_box.valueChanged.connect(self.canvas_view.set_stroke_width)
        self.canvas_mode_tools_ui.image_button.clicked.connect(self.canvas_view.set_image_tool)
        self.login_ui.github_button.clicked.connect(self.github_button_clicked)
        self.login_ui.discord_button.clicked.connect(self.discord_button_clicked)
        self.login_ui.twitter_button.clicked.connect(self.twitter_button_clicked)
        self.login_ui.create_new_user_button.clicked.connect(self.create_new_user_button_clicked)
  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Omniverse()
    window.show()
    sys.exit(app.exec())


    