import pygame
from sounddevice import InputStream
import importlib.resources
import io, os
from src.audio.tts.tts_manager import TTSManager
from src.audio.tts.pyttsx3_engine import Pyttsx3Engine

class AudioManager:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        # Initialize your InputStream for sounddevice here
        self.stream = None  # TODO: initialize InputStream
        self.sound_effects = {}
        self.load_all_sound_effects()

        self.tts_flag = False
        self.stt_flag = False

        self.pyttsx3 = Pyttsx3Engine()
        self.tts_manager = TTSManager(self.pyttsx3)

        print("AudioManager initialized")


    def load_all_sound_effects(self):
        """
        Load all sound effects from the resources.sounds directory.
        """
        with importlib.resources.path('resources', 'sounds') as sound_dir:
            for file_name in os.listdir(sound_dir):
                name, ext = os.path.splitext(file_name)
                if ext in ['.wav', '.mp3', '.ogg']:  # add other supported formats if needed
                    print(f"Loading sound effect: {name}")
                    self.load_sound_effect(name, file_name)


    def load_sound_effect(self, name, file_path):
        """
        Load a sound effect from a file and store it in the sound_effects dict.
        """
        file_data = importlib.resources.read_binary('resources.sounds', file_path)
        file_io = io.BytesIO(file_data)
    
        # Use pygame's Sound class to create a Sound object
        sound = pygame.mixer.Sound(file_io)
        self.sound_effects[name] = sound
        pass

    def play_sound_effect(self, name):
        """
        Play a sound effect by name.
        """
        if name in self.sound_effects:
            self.sound_effects[name].play()
        else:
            print(f"No sound effect with the name '{name}' was found.")
        pass

    def start_recording(self):
        """
        Start recording audio.
        """
        # TODO: implement
        pass

    def stop_recording(self):
        """
        Stop recording audio.
        """
        # TODO: implement
        pass

    def package_audio(self):
        """
        Package the recorded audio into files.
        """
        # TODO: implement
        pass

    def send_audio_to_whisper(self):
        """
        Send the packaged audio files to the Whisper API for speech-to-text conversion.
        """
        # TODO: implement
        pass

    def feed_to_llm(self, text):
        """
        Feed the converted text to the LLM chat client.
        """
        # TODO: implement
        pass
