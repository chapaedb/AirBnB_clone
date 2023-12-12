#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import os.path

class FileStorage:
    __file_path = os.path.join(os.getcwd(), "file.json")
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.id"
        self.__objects[key] = obj

    def default_serializer(self, obj):
        if isinstance(obj, BaseModel):
            return obj.to_dict()
        raise TypeError("Object of type {} is not JSON serializable".format(type(obj)))

    def save(self):
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(data, file, default=self.default_serializer)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                self.__objects = {}
                for key, value in data.items():
                    class_name, _ = key.split('.')
                    obj = globals()[class_name](**value)
                    self.__objects[key] = obj
