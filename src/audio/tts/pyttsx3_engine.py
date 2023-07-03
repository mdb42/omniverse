import pyttsx3
from PyQt6.QtCore import QThread, pyqtSignal
from src.audio.tts.tts_base import TTSBase

class PlaySpeechThread(QThread):
    def __init__(self, engine, text, parent=None):
        super().__init__(parent)
        self.engine = engine
        self.text = text

    def run(self):
        self.engine.say(self.text)
        self.engine.runAndWait()

class Pyttsx3Engine(TTSBase):
    def __init__(self):
        self.engine = pyttsx3.init()

    def get_available_voices(self):
        return [voice.id for voice in self.engine.getProperty('voices')]

    def set_voice(self, voice):
        self.engine.setProperty('voice', voice)

    def play_speech_sync(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def play_speech_async(self, text):
        self.thread = PlaySpeechThread(self.engine, text)
        self.thread.start()

    def stop_speech(self):
        self.engine.stop()

    def set_volume(self, volume):
        self.engine.setProperty('volume', volume)

    def set_rate(self, rate):
        self.engine.setProperty('rate', rate)
