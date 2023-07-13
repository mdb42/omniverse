import os
from cryptography.fernet import Fernet
from pathlib import Path
from datetime import datetime
from local import constants

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine
from passlib.context import CryptContext

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'    
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)
    online = Column(Boolean)
    openai_api_key = Column(EncryptedType(String, 'openai_api_key', AesEngine, 'pkcs5'))
    role = Column(String)
    created_at = Column(String)
    last_login = Column(String)


class SessionManager:
    """Manages the creation, reading, and writing of files and databases."""

    def __init__(self, app_name, key):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        # print("Pwd context: " + str(self.pwd_context))
        # Setup session variables
        self.start_time = datetime.now()
        self.base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'local')
        self.docs_dir = Path.home() / 'Documents' / app_name
        self.pref_dir = self.base_dir    
        self.users_db_path = os.path.join(self.base_dir, 'users.db')
        self.encryption_key = key
        self.current_user = None
        self.current_user_name = constants.DEFAULT_USER_NAME # Just for testing 
        self.preferred_output_dir = None
        self.engine = None
        self.session = None
        self.setup()

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
       
        # Check if the engine is already created
        if self.engine is None:
            # Create the engine
            self.engine = create_engine('sqlite:///' + self.users_db_path)        
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # if no users exist, create a default admin user
        if self.session.query(User).count() == 0:
            self.create_user("admin", "admin", "password", "None")
        
        
    def create_user(self, name, role, password, openai_api_key):
        """Creates a new user and adds them to the users database."""
        created_at = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        last_login = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        hashed_password = self.pwd_context.hash(password)

        user = User(name=name, 
                    password=hashed_password, 
                    openai_api_key=openai_api_key, 
                    online=False,
                    role=role, 
                    created_at=created_at, 
                    last_login=last_login)
        self.session.add(user)
        self.session.commit()

        self.current_user = user

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

    def is_admin(self, name):
        """Checks if a user is an admin."""
        user = self.session.query(User).filter_by(name=name).first()
        return user.role == 'admin'

    def get_all_users(self):
        """Returns all users in the database."""
        return self.session.query(User).all()
    
    def get_user_data(self, name):
        """Fetches a user's data based on their name."""
        user = self.session.query(User).filter_by(name=name).first()
        return user
    
    def delete_user(self, name):
        """Deletes a user from the database."""
        if not self.is_admin(self.current_user_name):
            raise Exception('Only admins can delete users.')
        user = self.session.query(User).filter_by(name=name).first()
        if user:
            self.session.delete(user)
            self.session.commit()

    def reset_password(self, name, new_password):
        """Resets a user's password."""
        user = self.session.query(User).filter_by(name=name).first()
        if user:
            hashed_password = self.pwd_context.hash(new_password)
            user.password = hashed_password
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



    
        

