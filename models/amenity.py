#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel"""

    def __init__(self):
        """
        Initializes a new instance of the Amenity class.
        """
        super().__init__()
        self.name = ""
