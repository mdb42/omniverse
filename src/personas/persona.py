import os

class Persona:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'Chat Bot')
        self.chain = None
        self.memory = None
        self.setup()
        print("Test Persona: Initialized")
    
    def setup(self):
        print("Test Persona: Setting Up Persona")
        pass

class PersonaFactory:
    def __init__(self, *args, **kwargs):
        self.session = kwargs.get('session', None)
        self.personas_dir = os.path.join(self.session.public_dir, "Personas")
        print("Test Persona Factory: Initialized")
