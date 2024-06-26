#!/usr/bin/env python3

import models
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime
import uuid


Base = declarative_base()


class BaseModel:
    __abstract__ = True
    id = Column(String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.utcnow())
        self.updated_at = kwargs.get('updated_at', datetime.utcnow())
        for k, val in kwargs.items():
            if k not in ['id', 'created_at', 'updated_at']:
                setattr(self, k, val)

    def save(self):
        """ Updates the attr 'updated_at' with the current datetime """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary contains keys and values of the instance """
        new_dict = {}
        for col in self.__table__.columns:
            value = getattr(self, col.name)
            if isinstance(value, datetime):
                value = value.isoformat()
            new_dict[col.name] = value
        return new_dict

    def delete(self):
        """ Deletes the current instance from the storage """
        models.storage.delete(self)
