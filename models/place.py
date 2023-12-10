#!/usr/bin/python3
from models.base_model import BaseModel
class Place(BaseModel):
    def __init__(self, city_id='', user_id=''):
        super().__init__()
        self.city_id = city_id
        self.user_id = user_id
        self.name = str()
        self.description = str()
        self.number_rooms = int(0)
        self.number_bathrooms = int(0)
        self.max_guest = int(0)
        self.price_by_night = int(0)
        self.latitude = float(0.0)
        self.longitude = float(0.0)
        self.amenity_id = [""]
