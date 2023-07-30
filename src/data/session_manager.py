import os
import sys
from datetime import datetime
from src.data.schema import User, Base, SecureKey, GalleryImage

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.context import CryptContext

from pathlib import Path
import src.data.data_utils as data_utils
from src.logger_utils import create_logger
from src import constants

# TODO: Implementing more granular user role management and permissions. Requires: user management widget
# TODO: Adding more features related to key management, like updating or removing a key. Requires: user settings widget with key table
# TODO: Improving logging or adding more detailed error handling. Requires: Deciding on a logging method.
# TODO: Implementing more features for the image gallery like saving, updating, or removing images. Requires: gallery widget
# TODO: Creating more detailed methods for manipulating and retrieving data. Requires: Exploring ways data might be used.
# TODO: Building out test cases to ensure that everything works as expected. Requires: Knowing the first thing about proper testing.

class SessionManager:
    """Manages the creation, reading, and writing of files and databases."""
    def __init__(self):
        self.logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)
        self.logger.info("Initializing Session Manager")
        self.start_time = datetime.now()
        # If the local directory exists, use it. Otherwise, use the user's documents directory.
        self.base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'local')
        if not os.path.exists(self.base_dir):
            self.base_dir = Path.home() / 'Documents' / constants.TITLE   
            data_utils.ensure_dir_exists(self.base_dir)

        self.public_dir = os.path.join(self.base_dir, 'Public')
        self.users_dir = os.path.join(self.base_dir, 'Users')
        self.users_db_path = os.path.join(self.users_dir, 'users.db')

        self.users_engine = None # The engine for the users database
        self.users_session = None # The session for the users database
        self.current_user = None 
        self.user_dir = None # The current user's personal directory

        self.vault_engine = None # The engine for the user's key vault database
        self.vault_session = None # The session for the user's key vault database

        self.gallery_path = os.path.join(self.public_dir, 'Images', 'gallery.db') # The path to the gallery database
        data_utils.ensure_dir_exists(os.path.join(self.public_dir, 'Images')) # Ensure the images directory exists
        self.gallery_engine = create_engine('sqlite:///' + self.gallery_path) # The engine for the gallery database
        Base.metadata.create_all(self.gallery_engine) # Create the gallery database
        Session = sessionmaker(bind=self.gallery_engine) # Create a session for the gallery database
        self.gallery_session = Session() # The session for the gallery database
        
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")        
        self.setup()
        self.logger.info("Session Manager initialized")

    def setup(self):
        """Sets up the data manager by creating the base directory and users database."""
        if not os.path.exists(self.base_dir):
            # Create the base directory
            data_utils.ensure_dir_exists(self.base_dir)
        
        self.create_workspace_directories()
       
        # Check if the engine is already created
        self.users_engine = create_engine('sqlite:///' + self.users_db_path)        
        Base.metadata.create_all(self.users_engine)
        Session = sessionmaker(bind=self.users_engine)
        self.users_session = Session()

    def create_workspace_directories(self):
        data_utils.ensure_dir_exists(self.users_dir)
        data_utils.ensure_dir_exists(self.public_dir)
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Blueprints"))) # For storing blueprint json files
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Images"))) # For the gallery database and image directories
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Images", "Generated"))) # For generated images
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Images", "Imported"))) # For imported images
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Images", "Saved"))) # For saved images created in canvas mode
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Personas"))) # Contains directories for each persona
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Prompts"))) # Contains directories for each prompt type
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Prompts", "Grounding"))) # Contains directories for grounding prompts
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Prompts", "Image"))) # Contains directories for image prompts
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Prompts", "Persona"))) # Contains directories for persona prompts
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Prompts", "Context"))) # Contains directories for protocol prompts
        data_utils.ensure_dir_exists(str(os.path.join(self.public_dir, "Worlds"))) # Contains directories for each world

    def create_user(self, name, role, input_password, api_key=None):
        """Creates a new user and adds them to the users database."""
        self.logger.info(f"Creating user {name}")
        if not name or not role or not input_password:
            raise ValueError("All fields are required")
        
        if self.users_session is not None and self.users_session.query(User).filter_by(name=name).first():
            raise ValueError(f"User {name} already exists")
        
        created_at = datetime.now()
        last_login = datetime.now()
        hashed_password = self.pwd_context.hash(input_password)
        encrypted_hashed_password = data_utils.encrypt(hashed_password)
        remember_me = False
        encrypted_remember_me = data_utils.encrypt(remember_me)

        user = User(name=name, 
                    password=encrypted_hashed_password,
                    remember_me=encrypted_remember_me,
                    role=role,
                    online=False,
                    display_name=name,
                    created_at=created_at, 
                    last_login=last_login)
        
        self.users_session.add(user)
        self.users_session.commit()
        self.current_user = user

        self.user_dir = os.path.join(self.users_dir, name)
        self.create_user_files()

        # The best syntax for making a string all lower case is

         # Let's make a key vault for the user
        vault_path = os.path.join(self.user_dir, f'{name.lower()}-vault.db')
        self.vault_engine = create_engine('sqlite:///' + vault_path)
        Base.metadata.create_all(self.vault_engine)
        Session = sessionmaker(bind=self.vault_engine)
        self.vault_session = Session()

        # Let's encrypt the api key and add it as the default key
        if self.vault_session is not None:
            encrypted_api_key = data_utils.encrypt(api_key)
            self.vault_session.add(SecureKey(name='default', 
                                             provider='OpenAI', 
                                             key=encrypted_api_key, 
                                             created_at=datetime.now(), 
                                             last_used=datetime.now()))
            self.vault_session.commit()

    def create_user_files(self):
        """Creates a user's output directory."""
        data_utils.ensure_dir_exists(self.user_dir)
        data_utils.ensure_dir_exists(str(os.path.join(self.user_dir, "Transcripts")))

       

    def login_user(self, name, password, remember_me):
        if not name or not password:
            self.logger.warning("Name and password are required")
            return False
                
        user = self.users_session.query(User).filter_by(name=name).first()
        if not user:
            self.logger.warning(f"User {name} does not exist")
            return False
        
        # Check if the user is not remembered or if the password is incorrect
        if not data_utils.decrypt(user.remember_me) and not self.pwd_context.verify(password, data_utils.decrypt(user.password)):
            self.logger.warning(f"Incorrect password for user {name}")
            return False
            
        user.online = True
        user.last_login = datetime.now()  
        user.remember_me = data_utils.encrypt(remember_me)  
        self.current_user = user
        self.user_dir = os.path.join(self.users_dir, name)
            
        self.users_session.commit()
        vault_path = os.path.join(self.user_dir, f'{name.lower()}-vault.db')
        self.vault_engine = create_engine('sqlite:///' + vault_path)
        Base.metadata.create_all(self.vault_engine)
        Session = sessionmaker(bind=self.vault_engine)
        self.vault_session = Session()

        return True

    def logout_user(self):
        if not self.current_user:
            raise ValueError("No user is currently logged in")
        self.current_user.online = False
        self.users_session.commit()
        self.current_user = None

    def is_admin(self, name):
        if not name:
            raise ValueError("All fields are required")
        user = self.users_session.query(User).filter_by(name=name).first()
        if not user:
            raise UserDoesNotExist(f"User {name} does not exist")        
        return user.role == 'Admin'

    def get_user_by_name(self, name):
        if self.users_session is not None and name:
            user = self.users_session.query(User).filter_by(name=name).first()
            return user
        else:
            return None

    def get_all_users(self):
        return self.users_session.query(User).all()
    
    def get_all_user_names_by_last_login(self):
        names = []
        if self.users_session is not None:
            for user in self.users_session.query(User).order_by(User.last_login.desc()):
                names.append(user.name)
            return names
        else:
            return None
    
    def delete_user(self, name):
        if not name:
            raise ValueError("All fields are required")
        user = self.users_session.query(User).filter_by(name=name).first()
        if not user:
            raise UserDoesNotExist(f"User {name} does not exist")
        if not self.is_admin(self.current_user.name):
            raise NotAdminUser('Only admins can delete users.')
        
        self.users_session.delete(user)
        self.users_session.commit()

    def close(self):
        self.logger.info("Closing database connection")
        if self.users_session is not None: self.users_session.close()
        if self.vault_session is not None: self.vault_session.close()
        if self.gallery_session is not None: self.gallery_session.close()
        if self.users_engine is not None: self.users_engine.dispose()
        if self.vault_engine is not None: self.vault_engine.dispose()
        if self.gallery_engine is not None: self.gallery_engine.dispose()
        self.logger.info("Database connection closed")

    def get_user_count(self):
        """Returns the number of users in the users database."""
        if self.users_session is not None:
            return self.users_session.query(User).count()
        else:
            return 0
    
    def get_most_recent_user(self):
        """Returns the most recently created user."""
        if self.users_session is not None:
            return self.users_session.query(User).order_by(User.created_at.desc()).first()
        else:
            return None
    
    def get_key_by_provider(self, provider):
        """Returns the user's key from the key vault."""
        if self.vault_session is not None:
            return self.vault_session.query(SecureKey).filter_by(provider=provider).first()
        else:
            return None
    
    



class UserDoesNotExist(Exception):
    pass

class IncorrectPassword(Exception):
    pass

class NotAdminUser(Exception):
    pass

class UserAlreadyExists(Exception):
    pass

class KeyDoesNotExist(Exception):
    pass

class KeyAlreadyExists(Exception):
    pass

class ImageDoesNotExist(Exception):
    pass

class ImageAlreadyExists(Exception):
    pass