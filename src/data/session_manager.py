import os
from cryptography.fernet import Fernet
from pathlib import Path
from datetime import datetime
from local import constants

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from passlib.context import CryptContext

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(EncryptedType(String, 'password', AesEngine, 'pkcs5'))
    openai_api_key = Column(EncryptedType(String, 'openai_api_key', AesEngine, 'pkcs5'))
    role = Column(String)
    created_at = Column(String)
    last_login = Column(String)
    time_zone = Column(String)
    preferred_output_dir = Column(String)
    preferred_pronouns = Column(String)
    avatar_path = Column(String)
    dark_mode = Column(String)
    preferred_llm = Column(String)
    preferred_llm_temperature = Column(String)
    chat_color = Column(String)
    bio = Column(String)
    email = Column(String)
    phone = Column(String)
    website = Column(String)

class SessionManager:
    """Manages the creation, reading, and writing of files and databases."""

    def __init__(self, app_name, key):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        print("Pwd context: " + str(self.pwd_context))
        # Setup session variables
        self.start_time = datetime.now()
        # base directory should be the project directory's local folder
        self.base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'local')
        print("Base dir: " + self.base_dir)
        self.docs_dir = Path.home() / 'Documents' / app_name
        print("Docs dir: " + str(self.docs_dir))
        self.pref_dir = self.base_dir    
        print("Pref dir: " + str(self.pref_dir))   
        self.users_db_path = os.path.join(self.base_dir, 'users.db')
        print("Users db path: " + self.users_db_path)
        self.encryption_key = key
        print("Encryption key: " + str(self.encryption_key))
        self.current_user = None
        print("Current user: " + str(self.current_user))
        self.current_user_name = constants.DEFAULT_USER_NAME # Just for testing   
        print("Current user name: " + str(self.current_user_name))     
        self.preferred_output_dir = None
        print("Preferred output dir: " + str(self.preferred_output_dir))
        self.engine = None
        print("Engine: " + str(self.engine))
        self.session = None
        print("Session: " + str(self.session))
        self.setup()
        print("Setup complete")

    ####################################################################################################
    # Database operations
    ####################################################################################################
    def setup(self):
        """Sets up the data manager by creating the base directory and users database."""
        # Check if the base directory exists
        os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY # We'll modify and move this to login method later
        

        if not os.path.exists(self.base_dir):
            # Create the base directory
            self.ensure_dir_exists(self.base_dir)
            # Create the users database

        print(str(self.base_dir))
        # Check if the engine is already created
        if self.engine is None:
            # Create the engine
            print("Creating engine")
            self.engine = create_engine('sqlite:///' + self.users_db_path)        
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # if no users exist, create a default admin user
        if self.session.query(User).count() == 0:
            print("No users found.")
            self.create_user("admin", "admin", "pasword", "None", os.path.join(self.base_dir, "private/admin"), "he/him")
            
        else:
            print("Users exist")
            # Let's print out all the users in the database by name
            for user in self.session.query(User).all():
                print(user.name)
        
        
            

    def create_user(self, name, role, password, openai_api_key, preferred_output_dir, preferred_pronouns):
        """Creates a new user and adds them to the users database."""
        created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        last_login = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        time_zone = datetime.now().strftime("%Z")
        preferred_output_dir = os.path.join(self.base_dir, name)
        hashed_password = self.pwd_context.hash(password)
        # When verifying the password during a login, you can use pwd_context.verify(input_password, stored_password)
        # which will return True if the input_password matches the stored_password after hashing.

        user = User(name=name, 
                    password=hashed_password, 
                    openai_api_key=openai_api_key, 
                    role=role, 
                    created_at=created_at, 
                    last_login=last_login, 
                    time_zone=time_zone, 
                    preferred_output_dir=preferred_output_dir, 
                    preferred_pronouns=preferred_pronouns)
        self.session.add(user)
        self.session.commit()

        self.current_user = user
        self.preferred_output_dir = user.preferred_output_dir

        # Create the user's output directories
        self.ensure_dir_exists(user.preferred_output_dir)
        self.ensure_dir_exists(str(os.path.join(self.preferred_output_dir, "images")))
        self.ensure_dir_exists(str(os.path.join(self.preferred_output_dir, "logs")))
        self.ensure_dir_exists(str(os.path.join(self.preferred_output_dir, "models")))
        self.ensure_dir_exists(str(os.path.join(self.preferred_output_dir, "transcripts")))
    
    def update_user(self, name, field, new_value):
        """Updates the specified field for a user."""
        user = self.session.query(User).filter_by(name=name).first()
        if user:
            setattr(user, field, new_value)
            self.session.commit()
    
    def login_user(self, name, password):
        """Logs in a user if the password is correct."""
        user = self.session.query(User).filter_by(name=name).first()
        if user and self.pwd_context.verify(password, user.password):
            self.current_user_name = user
            user.last_login = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
            self.session.commit()
            return True
        return False
    
    def logout_user(self):
        """Logs out the current user."""
        self.current_user_name = None

    def get_all_users(self):
        """Returns all users in the database."""
        return self.session.query(User).all()
    
    def get_user_data(self, name):
        """Fetches a user's data based on their name."""
        user = self.session.query(User).filter_by(name=name).first()
        return user
    
    def delete_user(self, name):
        """Deletes a user from the database."""
        user = self.session.query(User).filter_by(name=name).first()
        if user:
            self.session.delete(user)
            self.session.commit()
    



    ####################################################################################################
    # File operations
    ####################################################################################################

    def ensure_dir_exists(self, dir_path):
        """Ensures a directory exists, creating it if necessary."""
        os.makedirs(dir_path, exist_ok=True)

    def get_full_path(self, relative_path):
        """Returns the full path for a file or directory."""
        return os.path.join(self.base_dir, relative_path)

    def write_file(self, relative_path, data):
        """Writes data to a file."""
        full_path = self.get_full_path(relative_path)
        with open(full_path, 'w') as f:
            f.write(data)

    def read_file(self, relative_path):
        """Reads data from a file."""
        full_path = self.get_full_path(relative_path)
        with open(full_path, 'r') as f:
            return f.read()

    def write_encrypted_file(self, relative_path, data, key):
        """Writes encrypted data to a file."""
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))
        self.write_file(relative_path, encrypted_data.decode('utf-8'))

    def read_encrypted_file(self, relative_path, key):
        """Reads encrypted data from a file and returns the decrypted data."""
        cipher_suite = Fernet(key)
        encrypted_data = self.read_file(relative_path).encode('utf-8')
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return decrypted_data.decode('utf-8')



    
        

