
import json
from src.logger_utils import create_logger
from src import constants
class Blueprint:
    def __init__(self, *args, **kwargs):
        """Initialize Blueprint"""
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("Blueprint: Initializing")
        self.name = kwargs.get('name', 'Blueprint')
        self.description = kwargs.get('description', 'Blueprint Description')
        self.author = kwargs.get('author', 'Blueprint Author')
        self.created_at = kwargs.get('created_at', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.input = kwargs.get('input', None)
        self.variables = kwargs.get('variables', None)
        self.output = kwargs.get('output', None)
        self.steps = kwargs.get('steps', None)
        self.logger.info("Blueprint: Initialized")
    
    def load_from_json(self, blueprint_json):
        """ Load Blueprint from JSON"""
        try:
            blueprint_json_dict = json.loads(blueprint_json)
            for key, value in blueprint_json_dict.items():
                if key == 'blueprint':
                    for k, v in value.items():
                        setattr(self, k, v)
        except json.JSONDecodeError:
            self.logger.error(f"Blueprint: Error decoding Blueprint JSON: {blueprint_json}")

        
    