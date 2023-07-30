
from src.worlds.world_base import WorldBase

class World(WorldBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', "Unnamed World")
        self.description = kwargs.get('description', "Undescribed World")
        self.areas = kwargs.get('areas', [])
        self.personas = kwargs.get('personas', []) # references to personas in the world

