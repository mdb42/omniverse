from abc import ABC, abstractmethod

class BaseArtGenerator(ABC):
    @abstractmethod
    def generate_image(self, prompt: str):
        pass