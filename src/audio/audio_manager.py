import sounddevice as sd
import soundfile as sf
import importlib.resources
import os
from src.audio.tts.tts_manager import TTSManager
from src.audio.tts.pyttsx3_engine import Pyttsx3Engine

# Instead of using sd.play, we should set up a Stream object and use that to play audio.
# Docs: https://python-sounddevice.readthedocs.io/en/0.4.1/api.html#sounddevice.Stream
# Examples: https://snyk.io/advisor/python/sounddevice/functions/sounddevice.Stream
# The Stream object can be used to play audio asynchronously, with adjustable volume, etc.
# We should maintain (and periodically update) a list of all active devices.
# We need to identify the default output device and use that to play audio.
# Set the channels to match the device.
# Set the sample rate to match the sound file's sample rate.
# Set the dtype to match the sound file's dtype.
# Set the latency to match the file's latency.
# Set the blocksize to match the device's blocksize.
# Set the callback to match the device's callback.
# And we need to identify the default input device and use that to record audio.
# Wait on input implementation until we can study Whisper API to review expectations.
# We should also maintain a list of all active streams? Is that a thing? Multiple streams can be active at once?
# Audio output will be either sound effects intended for simultaneous playback, or music/long wav files for single playback.
# The sound effects need to be stored, but the music/long wav files can be loaded as needed (possibly managed locally as two fields, current_song and next_song).
# Otherwise playlists can be just lists of strings of songs by name.
# Ensure that the Stream object is closed when the program exits.

class AudioManager:
    def __init__(self):
        self.sound_effects = {}
        self.load_all_sound_effects()

        self.text_to_speech = False
        self.speech_to_text = False

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
                if ext in ['.wav', '.flac']:  # soundfile supports .wav and .flac primarily
                    print(f"Loading sound effect: {name}")
                    self.load_sound_effect(name, os.path.join(sound_dir, file_name))

    def load_sound_effect(self, name, file_path):
        """
        Load a sound effect from a file and store it in the sound_effects dict.
        """
        # Use soundfile's read function to load audio file into numpy array
        data, samplerate = sf.read(file_path, dtype='float32')
        self.sound_effects[name] = (data, samplerate)

    def play_sound_effect(self, name):
        """
        Play a sound effect, by name, asynchronously such that multiple instances of the
        same sound effect can be played simultaneously.
        """
        if name in self.sound_effects:
            data, samplerate = self.sound_effects[name]
            sd.play(data, samplerate)
            # sd.wait()
        else:
            print(f"No sound effect with the name '{name}' was found.")


    # Test implementation of Stream
    def play_sound_effect_stream(self, name):
        """
        Play a sound effect, by name, asynchronously such that multiple instances of the
        same sound effect can be played simultaneously.
        """
        if name in self.sound_effects:
            data, samplerate = self.sound_effects[name]
            stream = sd.Stream(samplerate=samplerate, dtype='float32', latency='low')
            stream.start()
            stream.write(data)
            stream.close()
        else:
            print(f"No sound effect with the name '{name}' was found.")
    
    def play_text_to_speech(self, text):
        """
        Play text to speech.
        """
        self.tts_manager.play_text(text)

    def start_text_to_speech(self):
        """
        Start text to speech.
        """
        self.tts_manager.start()

    def stop_text_to_speech(self):
        """
        Stop text to speech.
        """
        self.tts_manager.stop()
    
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

    def package_recording(self):
        """
        Package the recorded audio into files.
        """
        # TODO: implement
        return None
    
    def __del__(self):
        """
        Ensure all streams are closed when the AudioManager is deleted.
        """
        sd.stop()



