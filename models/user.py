#!/usr/bin/python3
from models.base_model import BaseModel
class user(BaseModel):
    def __init__(self):
        super().__init__()
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
