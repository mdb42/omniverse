import os
from cryptography.fernet import Fernet
from pathlib import Path
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

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

class DataManager:
    """Manages the creation, reading, and writing of files and databases."""

    def __init__(self, app_name, key):
        self.base_dir = Path.home() / 'Documents' / app_name      
        self.users_db_path = os.path.join(self.base_dir, 'users.db')
        self.encryption_key = key
        self.current_user = None
        self.preferred_output_dir = None
        self.engine = None
        self.session = None
        self.setup()


    def setup(self):
        """Sets up the data manager by creating the base directory and users database."""
        # Check if the base directory exists

        if not os.path.exists(self.base_dir):
            # Create the base directory
            self.ensure_dir_exists(self.base_dir)
        print(str(self.base_dir))
        
        self.engine = create_engine('sqlite:///' + self.users_db_path)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # if no users exist, create a default admin user
        if self.session.query(User).count() == 0:
            print("Creating default admin user")
            self.create_user("admin", "admin", "password", "None", os.path.join(self.base_dir, "admin"), "they/them")
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
        user = User(name=name, 
                    password=password, 
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



    
        

