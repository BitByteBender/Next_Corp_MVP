#!/usr/bin/env python3

from os import getenv
from models.engine.db_storage import session, create_all_tables

storage_type = getenv("NC_TYPE_STORAGE", "db")

if storage_type == "db":
    # Start DBStorage with the SQLAlchemy session
    class DBStorage:
        def __init__(self):
            self.session = session

        def reload(self):
            """ Reloads current session """
            create_all_tables()
            self.session = session

    storage_instance = DBStorage()

def storage():
    """ Returns the initialized storage object """
    if storage_type == "db":
        return storage_instance
    else:
        raise NotImplementedError("Other storage types are not implemented yet")
