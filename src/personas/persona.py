import os
from src.logger_utils import create_logger
from src import constants
from src.personas.blueprint import Blueprint
import json

class Persona:
    def __init__(self, *args, **kwargs):
        """Initialize Persona"""
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("Persona: Initializing")
        self.session = kwargs.get('session', None)
        self.name = kwargs.get('name', 'Chat Bot')
        self.description = kwargs.get('description', 'Chat Bot Persona')
        self.gender = kwargs.get('gender', None)
        self.creator = kwargs.get('creator', None)
        self.creation_date = kwargs.get('creation_date', None)
        self.blueprint_filename = kwargs.get('blueprint_filename', None)
        self.blueprint = kwargs.get('blueprint', None)
        self.chain = kwargs.get('chain', None)
        self.memory = kwargs.get('memory', None)
        self.logger.info(f"Persona: {self.name} Initialized")
    
    def setup(self):
        """Setup Persona, called upon login."""
        if self.blueprint == None and self.blueprint_filename != None:
            self.load_blueprint()

    def load_from_json(self, persona_json):
        """Load Persona from JSON"""
        persona_json_dict = json.loads(persona_json)
        for key, value in persona_json_dict.items():
            if key == 'persona':
                for k, v in value.items():
                    setattr(self, k, v)

    def load_blueprint(self):
        """Create Blueprint for Persona"""
        self.logger.info(f"Persona: Loading Blueprint: {self.blueprint_filename}")
        blueprint_path = os.path.join(self.session.public_dir, "Blueprints", self.blueprint_filename)
        if os.path.exists(blueprint_path):
            try:
                # Attempt to open and read the blueprint JSON file
                with open(blueprint_path, "r") as f:
                    blueprint_json = f.read()
                    self.blueprint = Blueprint()
                    self.blueprint.load_from_json(blueprint_json)
            except Exception as e:
                # Log any exceptions that occur
                self.logger.error(f"Persona: Error reading from Blueprint JSON file {blueprint_path} : {e}")


