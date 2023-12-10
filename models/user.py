#!/usr/bin/python3
from base_model import BaseModel
class user(BaseModel):
    def __init__(self):
        super().__init__()
        self.email = str()
        self.password = str()
        self.first_name = str()
        self.last_name = str()
