# Test LLM Manager
import os
from src.personas.persona import Persona
from src.logger_utils import create_logger
from src import constants

class PersonaManager:
    def __init__(self, *args, **kwargs):
        """Initialize Persona Manager"""
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("Persona Manager: Initializing")
        self.session = kwargs.get('session', None)
        self.personas_dir = os.path.join(self.session.public_dir, "Personas")
        self.personas = self.create_workspace_personas()
        self.logger.info("Persona Manager: Initialized")
        self.current_responder = self.personas[0]

    def setup(self):
        """Setup Persona Manager and all Personas, called upon login."""
        for persona in self.personas:
            persona.setup()

    def generate_response(self, persona_name, context):
        """Generate a response from a Persona given a context."""
        self.logger.info("Persona Manager: Generating Response")
        return "Persona Manager: Response (Not Implemented))"
    
    def create_workspace_personas(self):
        """Create Personas from the workspace directory."""
        self.logger.info("Persona Factory: Loading Workspace Personas")
        personas = []
        for persona_name in os.listdir(self.personas_dir):
            self.logger.info(f"Persona Factory: Loading Persona: {persona_name}")
            persona = self.load_persona(name=persona_name)
            personas.append(persona)
        return personas
    
    def load_persona(self, name):
        """Load a Persona from the workspace directory."""
        self.logger.info(f"Persona Factory: Creating Persona: {name}")
        persona = Persona(session=self.session, name=name)
        json_path = os.path.join(self.personas_dir, name, f"{name.lower()}.json")
        if os.path.exists(json_path):
            try:
                # Attempt to open and read the JSON file
                with open(json_path, "r") as f:
                    persona_json = f.read()
                    persona.load_from_json(persona_json)
            except Exception as e:
                # Log any exceptions that occur
                self.logger.error(f"Persona Factory: Error reading from Persona JSON file {json_path} : {e}") 
        return persona
    
    def get_persona_names(self):
        """Get a list of Persona names."""
        names = []
        for persona in self.personas:
            names.append(persona.name)
        return names
    
    def set_current_responder(self, name):
        """Set the current responder."""
        for persona in self.personas:
            if persona.name == name:
                self.current_responder = persona
                return True
        return False

    