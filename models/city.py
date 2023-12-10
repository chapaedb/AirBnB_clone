#!/usr/bin/python3
from models.base_model import BaseModel
class City(BaseModel):
    def __init__(self, state_id=''):
        super().__init__()
        self.state_id = state_id
        self.name = str()
