import abc

class TTSBase(abc.ABC):
    @abc.abstractmethod
    def get_available_voices(self):
        pass

    @abc.abstractmethod
    def set_voice(self, voice):
        pass

    @abc.abstractmethod
    def play_speech_sync(self, text):
        pass

    @abc.abstractmethod
    def play_speech_async(self, text):
        pass

    @abc.abstractmethod
    def stop_speech(self):
        pass

    @abc.abstractmethod
    def set_volume(self, volume):
        pass

    @abc.abstractmethod
    def set_rate(self, rate):
        pass