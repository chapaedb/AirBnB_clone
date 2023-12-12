#!/usr/bin/python3
from models.base_model import BaseModel

class State(BaseModel):
    """State class that inherits from BaseModel"""

    def __init__(self):
        """
        Initializes a new instance of the State class.
        """
        super().__init__()
        self.name = ""
