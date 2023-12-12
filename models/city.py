#!/usr/bin/python3
from models.base_model import BaseModel

class City(BaseModel):
    """City class that inherits from BaseModel"""

    def __init__(self, state_id=''):
        """
        Initializes a new instance of the City class.

        Args:
            state_id (str): State ID.
        """
        super().__init__()
        self.state_id = state_id
        self.name = ''
