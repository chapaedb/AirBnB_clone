#!/usr/bin/python3
from models.base_model import BaseModel
class Review(BaseModel):
    def __init__(self, place_id='', user_id=''):
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = str()
