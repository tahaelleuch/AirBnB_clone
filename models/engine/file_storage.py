#!/usr/bin/python3
import json
import os.path
from models.base_model import BaseModel
"""
classe de stockage dans un fichier json
"""


class FileStorage:
    """ constructeur prametré """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ retourne un objet  de dictionaire"""
        return (self.__objects)

    def new(self, obj):
        """ ajouter un objet dans le dictionnaire"""
        if obj is None:
            pass
        else:
            cle = obj.__class__.__name__ + "." + obj.id
            self.__objects[cle] = obj

    def save(self):
        """serializé les objet en json"""
        dic_object = {}
        for key, value in self.__objects.items():
            dic_object[key] = value.to_dict()	
        with open(self.__file_path, mode='w') as fichier:
            json.dump(dic_object, fichier)

    def reload(self):
        """ desirialization de json vers un objet"""
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_objects = json.load(f)
            for key in json_objects:
                self.__objects[key] = BaseModel(**json_objects[key])
        except:
            pass
