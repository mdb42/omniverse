import os
from cryptography.fernet import Fernet
from src import constants
import keyring
from src.logger_utils import create_logger

logger = create_logger(__name__, constants.SYSTEM_LOG_FILE)

# TODO: If we should need to encrypt/decrypt data other than strings and booleans, we'll employ json encoding.
    
def ensure_dir_exists(dir_path):
    """Ensures a directory exists, creating it if necessary."""
    os.makedirs(dir_path, exist_ok=True)
    
def get_full_path(base_path, relative_path):
    """Returns the full path for a file or directory."""
    return os.path.join(base_path, relative_path)

def write_file(base_path, relative_path, data):
    """Writes data to a file."""
    full_path = get_full_path(base_path, relative_path)
    try:
        with open(full_path, "w") as f:
            f.write(data)
    except IOError as e:
        logger.error(f"Error writing to file {full_path}: {e}")

def read_file(base_path, relative_path):
    """Reads data from a file."""
    full_path = get_full_path(base_path, relative_path)
    try:
        with open(full_path, "r") as f:
            data = f.read()
        return data
    except IOError as e:
        logger.error(f"Error reading from file {full_path}: {e}")
        return None

def write_encrypted_file(base_path, relative_path, data):
    """Writes encrypted data to a file."""
    full_path = get_full_path(base_path, relative_path)
    try:
        encrypted_data = encrypt(data)
        if encrypted_data is None:
            raise ValueError("Encryption failed")
        with open(full_path, "wb") as f:
            f.write(encrypted_data)
    except (IOError, ValueError) as e:
        logger.error(f"Error writing encrypted data to file {full_path}: {e}")

def read_encrypted_file(base_path, relative_path):
    """Reads encrypted data from a file and returns the decrypted data."""
    full_path = get_full_path(base_path, relative_path)
    try:
        with open(full_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = decrypt(encrypted_data)
        if decrypted_data is None:
            raise ValueError("Decryption failed")
        return decrypted_data
    except (IOError, ValueError) as e:
        logger.error(f"Error reading encrypted data from file {full_path}: {e}")
        return None

def encrypt(data):
    key_string = keyring.get_password(constants.TITLE, constants.WORKSPACE)
    # Convert the key back to bytes
    key_bytes = key_string.encode()
    cypher_suite = Fernet(key_bytes)
    # Ensure data is bytes
    if isinstance(data, bool):
        data = str(data).encode('utf-8')
    elif not isinstance(data, bytes):
        data = data.encode('utf-8')
    encrypted_data = cypher_suite.encrypt(data)
    return encrypted_data

def decrypt(encrypted_data):
    key_string = keyring.get_password(constants.TITLE, constants.WORKSPACE)
    # Convert the key back to bytes
    if key_string is not None:
        key_bytes = key_string.encode()
        cypher_suite = Fernet(key_bytes)
        data = cypher_suite.decrypt(encrypted_data)
        # Convert data back to string
        decrypted_data = data.decode('utf-8')
        # Convert "True"/"False" back to boolean
        if decrypted_data == "True":
            return True
        elif decrypted_data == "False":
            return False
        else:
            return decrypted_data
    else:
        logger.warning("Key not found in keyring")
        return None
