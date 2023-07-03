class TTSManager:
    def __init__(self, tts_engine, default_voice=None, default_volume=1, default_rate=150):
        self.tts_engines = [tts_engine]
        self.tts_engine = tts_engine
        self.default_voice = default_voice or self.tts_engine.get_available_voices()[0]
        self.tts_engine.set_voice(self.default_voice)

        self.set_volume(default_volume)
        self.set_rate(default_rate)

    def get_available_voices(self):
        return self.tts_engine.get_available_voices()

    def set_voice(self, voice):
        if voice:
            self.tts_engine.set_voice(voice)

    def play_speech_sync(self, text):
        if text:
            self.tts_engine.play_speech_sync(text)

    def play_speech_async(self, text):
        if text:
            self.tts_engine.play_speech_async(text)

    def stop_speech(self):
        self.tts_engine.stop_speech()

    def set_volume(self, volume):
        if 0 <= volume <= 1:
            self.tts_engine.set_volume(volume)

    def set_rate(self, rate):
        if rate > 0:
            self.tts_engine.set_rate(rate)
