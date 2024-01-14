#!/usr/bin/python3
"""This is the Base Model class"""

from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Base Class from which all other classes will inherit from """

    def __init__(self, *args, **kwargs):
        """ Initialises the instance attributes

        Args:
            *args: list of arguments
            **kwargs: dict of key-value arguments
        """
        dtform = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], dtform)
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], dtform)
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns official string representation of the Base model class"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all instances of __dict__ """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = type(self).__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        return my_dict
