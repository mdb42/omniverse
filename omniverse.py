import sys, os
from src.gui import omniverse_main
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPixmap, QIcon, QImage, QTextCursor
from PyQt6.QtCore import QTimer
import importlib.resources
from datetime import datetime
from src.llms.llm_manager import LLMManager
from src.audio.audio_manager import AudioManager
from src.art.art_manager import ArtManager
from local import constants
from langchain.callbacks.base import BaseCallbackManager
from src.gui.streaming_browser_out import StreamingBrowserCallbackHandler


TITLE = "Omniverse"
VERSION = "0.0.2"
FRAMES_PER_SECOND = 66

class Omniverse(QtWidgets.QMainWindow, omniverse_main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Omniverse, self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.setWindowTitle(f"{TITLE} {VERSION}")

        os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
        
        # Setup icons
        self.application_icon_pixmap = QPixmap()
        self.tts_on_button_icon_pixmap = QPixmap()
        self.tts_off_button_icon_pixmap = QPixmap()
        self.stt_on_button_icon_pixmap = QPixmap()
        self.stt_off_button_icon_pixmap = QPixmap()
        self.setup_icons()
        self.setup_signals()

        # Setup session variables
        self.session_start_time = datetime.now()
        self.user_id = constants.DEFAULT_USER_NAME
        self.assistant_id = constants.DEFAULT_AI_NAME
        self.tts_flag = False
        self.stt_flag = False

        # Setup the language model manager
        self.response_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.response_text_browser)])
        self.sentiment_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.sentiment_browser)])
        self.entity_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.entity_browser)])
        self.knowledge_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.knowledge_browser)])
        self.summary_cb = BaseCallbackManager([StreamingBrowserCallbackHandler(self.summary_browser)])

        self.browser_callbacks = {
            "response": self.response_cb,
            "sentiment": self.sentiment_cb,
            "entity": self.entity_cb,
            "knowledge": self.knowledge_cb,
            "summary": self.summary_cb
        }

        self.llm_manager = LLMManager(self.browser_callbacks, self.user_id, self.assistant_id)
        self.current_input = ""
        self.current_response = ""

        # Setup the AI art manager
        self.art_manager = ArtManager()        
        self.current_image = None

        # Setup the audio manager
        self.audio_manager = AudioManager()
        self.audio_manager.play_sound_effect("click")       
        
        # Initialize a QTimer for animation
        self.animation_timer = QTimer(self)
        self.animation_timer.timeout.connect(self.advance)
        self.animation_timer.start(int(1000/FRAMES_PER_SECOND))

    def advance(self):
        delta_time = self.animation_timer.interval() / 1000.0
        self.main_graphics_view.advance(delta_time)
  
    def generate_response(self):
        self.current_input = self.input_text_editor.toPlainText().rstrip()
        self.response_text_browser.append("\n" + str(self.user_id + ": " + self.current_input + "\n"))
        self.input_text_editor.clear()
        self.input_text_editor.setFocus()
        """ Generate a response from the LLM Manager."""
        print("Generating Response")
        self.set_cursor_to_end(self.response_text_browser)
        self.response_text_browser.append(self.assistant_id + ": ")
        self.preprocessing()
        self.current_response = self.llm_manager.generate_response()
        self.postprocessing()
        self.llm_manager.report_tokens()

    def preprocessing(self):
        """ Perform all preprocessing events, ending with the LLM preprocessor."""
        print("Preprocessing Prompt Grounding")
        self.sentiment_browser.clear()
        self.entity_browser.clear()
        QtWidgets.QApplication.processEvents()
        self.llm_manager.preprocessing(self.current_input)

    def postprocessing(self):
        """ Perform all postprocessing events, ending with the LLM postprocessor."""
        print("Postprocessing Model Output")
        # if self.tts_checkbox.isChecked():
        #     self.tts_manager.play_speech_async(self.current_response)
        self.summary_browser.clear()
        self.knowledge_browser.clear()
        QtWidgets.QApplication.processEvents()
        print("Going to LLM Manager Post Processing")
        self.llm_manager.postprocessing(self.current_input, self.current_response)
        print("Finished LLM Manager Post Processing")
    
    def set_cursor_to_end(self, browser):
        cursor = browser.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        browser.setTextCursor(cursor)
        browser.ensureCursorVisible()
    
    def generate_image(self):
        print("Generating image")
 
    def toggle_draw_mode(self):
        self.main_graphics_view.draw_mode = True
        self.main_graphics_view.present_mode = not self.main_graphics_view.draw_mode
        self.draw_button.setChecked(self.main_graphics_view.draw_mode)
        self.present_button.setChecked(self.main_graphics_view.present_mode)        
        if self.main_graphics_view.draw_mode:
            self.draw_mode_widget.setVisible(True)
        else:
            self.draw_mode_widget.setVisible(False)
    
    def toggle_present_mode(self):
        self.main_graphics_view.present_mode = True
        self.main_graphics_view.draw_mode = not self.main_graphics_view.present_mode
        self.draw_button.setChecked(self.main_graphics_view.draw_mode)
        self.present_button.setChecked(self.main_graphics_view.present_mode)
        if self.main_graphics_view.present_mode:
            self.draw_mode_widget.setVisible(False)
        else:
            self.draw_mode_widget.setVisible(True)
    
    def toggle_tts_mode(self):
        self.tts_flag = not self.tts_flag
        if self.tts_flag:
            self.tts_mode_button.setIcon(QIcon(self.tts_on_button_icon_pixmap))
        else:
            self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

    def toggle_stt_mode(self):
        self.stt_flag = not self.stt_flag
        if self.stt_flag:
            self.stt_mode_button.setIcon(QIcon(self.stt_on_button_icon_pixmap))
        else:
            self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))
       
    def setup_icons(self):
        # Setup the application icon
        icon_data = importlib.resources.read_binary("resources.icons", "application-icon.ico")
        icon_image = QImage.fromData(icon_data)
        self.application_icon_pixmap = QPixmap.fromImage(icon_image)
        self.setWindowIcon(QIcon(self.application_icon_pixmap))
        
        # Setup the dynamic button icons
        tts_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-tts-on.ico")
        tts_on_button_icon_image = QImage.fromData(tts_on_button_icon_data)
        self.tts_on_button_icon_pixmap = QPixmap.fromImage(tts_on_button_icon_image)

        tts_off_button_icon_data = importlib.resources.read_binary("resources.icons", "button-tts-off.ico")
        tts_off_button_icon_image = QImage.fromData(tts_off_button_icon_data)
        self.tts_off_button_icon_pixmap = QPixmap.fromImage(tts_off_button_icon_image)
        self.tts_mode_button.setIcon(QIcon(self.tts_off_button_icon_pixmap))

        stt_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-on.ico")
        stt_on_button_icon_image = QImage.fromData(stt_on_button_icon_data)
        self.stt_on_button_icon_pixmap = QPixmap.fromImage(stt_on_button_icon_image)

        stt_off_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-off.ico")
        stt_off_button_icon_image = QImage.fromData(stt_off_button_icon_data)
        self.stt_off_button_icon_pixmap = QPixmap.fromImage(stt_off_button_icon_image)
        self.stt_mode_button.setIcon(QIcon(self.stt_off_button_icon_pixmap))

        stt_on_button_icon_data = importlib.resources.read_binary("resources.icons", "button-stt-on.ico")
        stt_on_button_icon_image = QImage.fromData(stt_on_button_icon_data)
        self.stt_on_button_icon_pixmap = QPixmap.fromImage(stt_on_button_icon_image)
        
        # Setup static button icons
        draw_button_icon_data = importlib.resources.read_binary("resources.icons", "mode-draw.ico")
        draw_button_icon_image = QImage.fromData(draw_button_icon_data)
        self.draw_button.setIcon(QIcon(QPixmap.fromImage(draw_button_icon_image)))

        present_button_icon_data = importlib.resources.read_binary("resources.icons", "mode-present.ico")
        present_button_icon_image = QImage.fromData(present_button_icon_data)
        self.present_button.setIcon(QIcon(QPixmap.fromImage(present_button_icon_image)))

        pencil_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-pencil.ico")
        pencil_button_icon_image = QImage.fromData(pencil_button_icon_data)
        self.pencil_button.setIcon(QIcon(QPixmap.fromImage(pencil_button_icon_image)))

        erase_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-eraser.ico")
        erase_button_icon_image = QImage.fromData(erase_button_icon_data)
        self.erase_button.setIcon(QIcon(QPixmap.fromImage(erase_button_icon_image)))
        
        line_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-line.ico")
        line_button_icon_image = QImage.fromData(line_button_icon_data)
        self.line_button.setIcon(QIcon(QPixmap.fromImage(line_button_icon_image)))
        
        ellipse_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-circle.ico")
        ellipse_button_icon_image = QImage.fromData(ellipse_button_icon_data)
        self.ellipse_button.setIcon(QIcon(QPixmap.fromImage(ellipse_button_icon_image)))

        rectangle_button_icon_data = importlib.resources.read_binary("resources.icons", "tool-square.ico")
        rectangle_button_icon_image = QImage.fromData(rectangle_button_icon_data)
        self.rectangle_button.setIcon(QIcon(QPixmap.fromImage(rectangle_button_icon_image)))

        undo_button_icon_data = importlib.resources.read_binary("resources.icons", "button-undo.ico")
        undo_button_icon_image = QImage.fromData(undo_button_icon_data)
        self.undo_button.setIcon(QIcon(QPixmap.fromImage(undo_button_icon_image)))

        redo_button_icon_data = importlib.resources.read_binary("resources.icons", "button-redo.ico")
        redo_button_icon_image = QImage.fromData(redo_button_icon_data)
        self.redo_button.setIcon(QIcon(QPixmap.fromImage(redo_button_icon_image)))

        clear_button_icon_data = importlib.resources.read_binary("resources.icons", "button-clear.ico")
        clear_button_icon_image = QImage.fromData(clear_button_icon_data)
        self.clear_button.setIcon(QIcon(QPixmap.fromImage(clear_button_icon_image)))

        generate_text_button_icon_data = importlib.resources.read_binary("resources.icons", "button-generate-text.ico")
        generate_text_button_icon_image = QImage.fromData(generate_text_button_icon_data)
        self.generate_text_button.setIcon(QIcon(QPixmap.fromImage(generate_text_button_icon_image)))

        generate_image_button_icon_data = importlib.resources.read_binary("resources.icons", "button-generate-image.ico")
        generate_image_button_icon_image = QImage.fromData(generate_image_button_icon_data)
        self.generate_image_button.setIcon(QIcon(QPixmap.fromImage(generate_image_button_icon_image)))

    def setup_signals(self):
        # Connect button click signals to methods
        self.stroke_color_button.color_changed.connect(self.main_graphics_view.set_tool_color)        
        self.stroke_width_spin_box.valueChanged.connect(self.main_graphics_view.set_stroke_width)
        self.pencil_button.clicked.connect(self.main_graphics_view.set_pencil_tool)
        self.erase_button.clicked.connect(self.main_graphics_view.set_erase_tool)
        self.rectangle_button.clicked.connect(self.main_graphics_view.set_rectangle_tool)
        self.ellipse_button.clicked.connect(self.main_graphics_view.set_ellipse_tool)
        self.line_button.clicked.connect(self.main_graphics_view.set_line_tool)
        self.undo_button.clicked.connect(self.main_graphics_view.undo)
        self.redo_button.clicked.connect(self.main_graphics_view.redo)
        self.main_graphics_view.undoAvailable.connect(self.undo_button.setEnabled)
        self.main_graphics_view.redoAvailable.connect(self.redo_button.setEnabled)
        self.draw_button.clicked.connect(self.toggle_draw_mode)
        self.present_button.clicked.connect(self.toggle_present_mode)
        self.clear_button.clicked.connect(self.main_graphics_view.clear)
        self.tts_mode_button.clicked.connect(self.toggle_tts_mode)
        self.stt_mode_button.clicked.connect(self.toggle_stt_mode)
        self.generate_text_button.clicked.connect(self.generate_response)
        self.generate_image_button.clicked.connect(self.generate_image)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Omniverse()
    window.show()
    sys.exit(app.exec())
    