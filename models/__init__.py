#!/usr/bin/python3

from os import getenv
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

storage_t = getenv("NC_TYPE_STORAGE")

if storage_t == "db":
    storage = DBStorage()
else:
    storage = FileStorage()

def initialize_storage():
    """
    Initialize or reloads storage instance.
    """
    storage.reload()

initialize_storage()
