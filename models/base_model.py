#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
description de la classe  de base
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ constructeur parametré"""
        if kwargs:
            for cle, valeur in kwargs.items():
                if cle == "__class__":
                    pass
                elif ((cle == "created_at") and isinstance(kwargs["created_at"], str)):
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    continue
                elif (cle is "updated_at") and isinstance(kwargs["updated_at"], str):
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                    continue
                else:
                    setattr(self, cle, valeur)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """ fonction daffichage """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ update de update_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ dictionnaire contient toutes les cases"""
        nouveaudictionaire = dict(self.__dict__)
        nouveaudictionaire["__class__"] = self.__class__.__name__
        nouveaudictionaire["created_at"] = self.created_at.isoformat()
        nouveaudictionaire["updated_at"] = self.updated_at.isoformat()
        return (nouveaudictionaire)
