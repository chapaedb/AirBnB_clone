#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import BaseModel
class Amenity(BaseModel):
    def __init__(self):
        super().__init__()
        self.name = str()
