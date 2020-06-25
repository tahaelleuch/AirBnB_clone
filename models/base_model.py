import uuid
from datetime import datetime
"""
description de la classe  de base
"""


class BaseModel:
    def __init__(self):
        """ constructeur parametré"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ fonction daffichage """
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """ update de update_at"""
        self.updated_at = datetime.now()

    def todict(self):
        """ dictionnaire contient toutes les cases"""
        nouveaudictionaire = dict(self.__dict__)
        nouveaudictionaire["__class__"] = self.__class__.__name__
        nouveaudictionaire["create_at"] = self.created_at.isoformat()
        nouveaudictionaire["updated_at"] = self.updated_at.isoformat()
        return (nouveaudictionaire)
