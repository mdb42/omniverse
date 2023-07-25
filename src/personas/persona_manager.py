# Test LLM Manager
import os
from src.personas.persona import Persona, PersonaFactory

class PersonaManager:
    def __init__(self, *args, **kwargs):
        self.session = kwargs.get('session', None)
        self.personas = []
        self.persona_factory = PersonaFactory(session=self.session)
        for persona_name in os.listdir(os.path.join(self.session.public_dir, "Personas")):
            print("Persona Manager: Loading Persona: " + persona_name)
            persona = Persona(name=persona_name)
            self.personas.append(persona)

        self.setup()
        print("Persona Manager: Initialized")

    def setup(self):
        print("Persona Manager: Setting Up Persona Manager")
        pass

    def generate_response(persona, context):
        print("Persona Manager: Generating Response for Persona: " + persona)
        return "Persona Manager: Response"

    