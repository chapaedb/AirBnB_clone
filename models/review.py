#!/usr/bin/python3
from models.base_model import BaseModel

class Review(BaseModel):
    """Review class that inherits from BaseModel"""

    def __init__(self, place_id='', user_id=''):
        """
        Initializes a new instance of the Review class.

        Args:
            place_id (str): Place ID.
            user_id (str): User ID.
        """
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = ""
