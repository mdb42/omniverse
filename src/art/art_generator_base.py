from abc import ABC, abstractmethod

class ArtGeneratorBase(ABC):
    @abstractmethod
    def generate_image(self, prompt: str):
        pass