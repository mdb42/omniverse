from abc import ABC, abstractmethod

class WorldBase(ABC):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "World Base")
        self.description = kwargs.get('description', "World Base")
    
    @abstractmethod
    def advance(self, *args, **kwargs):
        pass
    