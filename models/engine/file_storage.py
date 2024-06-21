#!/usr/bin/env python3

from os import getenv
from models.engine.db_storage import session, create_all_tables
from models.engine.file_storage import FileStorage

# Storage type to use based on environment variable or configuration
storage_type = getenv("NC_TYPE_STORAGE", "db")

if storage_type == "db":
    class DBStorage:
        def __init__(self):
            self.session = session

        def reload(self):
            """ Reloads current session """
            create_all_tables()
            self.session = session

    storage = DBStorage()

elif storage_type == "file":
    class FileStorage:
        def __init__(self):
            pass
        
        def read_data(self, filename):
            """ Method to read data from a file """
            pass
        
        def write_data(self, filename, data):
            """ Method to write data to a file """
            pass
    
    storage = FileStorage()

def get_storage():
    """ Returns initialized storage object """
    return storage
