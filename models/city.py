#!/usr/bin/python3
""" City Module for HBNB project """

import sys
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """This class represents a city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)


    def __init__(self, *args, **kwargs):
        """Initialization of city"""
        super().__init__(*args, **kwargs)
