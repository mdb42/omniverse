import os
from src.worlds.world import World
from src.logger_utils import create_logger
from src import constants

class WorldManager:
    def __init__(self, *args, **kwargs):
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("World Manager: Initializing")
        self.session = kwargs.get('session', None)
        self.worlds_dir = os.path.join(self.session.public_dir, "Worlds")
        self.worlds = self.create_workspace_worlds()
        self.logger.info("World Manager: Initialized")
    
    def setup(self):
        """Setup World Manager and all Worlds, called upon login."""
        for world in self.worlds:
            world.setup()
        
    def create_workspace_worlds(self):
        """Create Worlds from the workspace directory."""
        self.logger.info("World Factory: Loading Workspace Worlds")
        worlds = []
        for world_name in os.listdir(self.worlds_dir):
            self.logger.info(f"World Factory: Loading World: {world_name}")
            world = self.load_world(name=world_name)
            worlds.append(world)
        return worlds