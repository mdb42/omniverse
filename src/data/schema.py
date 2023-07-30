from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    password = Column(String)
    remember_me = Column(String)
    role = Column(String)
    online = Column(Boolean)
    display_name = Column(String)
    created_at = Column(DateTime)
    last_login = Column(DateTime)

class SecureKey(Base):
    __tablename__ = 'key_vault'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    provider = Column(String)
    key = Column(String)
    created_at = Column(DateTime)
    last_used = Column(DateTime)

class GalleryImage(Base):
    __tablename__ = 'gallery_images'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    file_path = Column(String)
    creator = Column(String)
    created_at = Column(DateTime)