#!/usr/bin/python3
import json
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.id"
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.__dict__
        with open(self.__file_path, 'w') as file:
            json.dump(data, file)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = {}
                for key, value in data.items():
                    class_name, _ = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
