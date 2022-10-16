#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = []
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
            cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state", single_parent=True)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
            @property
            def cities(self):
                ''' Getter attribute to retrieve City object '''
                all_objects = models.storage.all(City)
                city_list = [v for k, v in all_objects.items() if v.state_id == self.id]
                return city_list
