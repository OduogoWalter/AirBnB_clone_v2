#!/usr/bin/python3
"""Amenity Module for HBNB project"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that represents amenities offered in a place."""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
