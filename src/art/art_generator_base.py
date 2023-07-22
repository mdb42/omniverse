from abc import ABC, abstractmethod

class ArtGeneratorBase(ABC):
    def __init__(self, *args, **kwargs):
        self.session = kwargs.get('session', None)
        
    @abstractmethod
    def generate_image(self, prompt: str):
        pass