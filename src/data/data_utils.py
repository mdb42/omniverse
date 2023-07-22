
import os
import sys
from cryptography.fernet import Fernet
import keyring
from pathlib import Path

    
def ensure_dir_exists(dir_path):
    """Ensures a directory exists, creating it if necessary."""
    os.makedirs(dir_path, exist_ok=True)
    
def get_full_path(base_path, relative_path):
    """Returns the full path for a file or directory."""
    return os.path.join(base_path, relative_path)

def write_file(base_path, relative_path, data):
    """Writes data to a file."""
    full_path = get_full_path(base_path, relative_path)
    with open(full_path, "w") as f:
        f.write(data)


def read_file(base_path, relative_path):
    """Reads data from a file."""
    full_path = get_full_path(base_path, relative_path)
    with open(full_path, "r") as f:
        data = f.read()
    return data

def write_encrypted_file(base_path, relative_path, data):
    """Writes encrypted data to a file."""
    full_path = get_full_path(base_path, relative_path)
    encrypted_data = encrypt(data)
    with open(full_path, "wb") as f:
        f.write(encrypted_data)

def read_encrypted_file(base_path, relative_path):
    """Reads encrypted data from a file and returns the decrypted data."""
    full_path = get_full_path(base_path, relative_path)
    with open(full_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = decrypt(encrypted_data)
    return decrypted_data

def encrypt(data):
    key_string = keyring.get_password("Omniverse", "Workspace")
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
    key_string = keyring.get_password("Omniverse", "Workspace")
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
        return None





