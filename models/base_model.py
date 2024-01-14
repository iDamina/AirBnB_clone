#!/usr/bin/python3
"""Module for Base class
Contains the Base class for the AirBnB clone console.
"""

import uuid
from datetime import datetime


class BaseModel:

        """Class for base model of object hierarchy."""

            def __init__(self, *args, **kwargs):
                        """Initialization of a Base instance.
                                Args:
                                            - *args: list of arguments
                                                        - **kwargs: dict of key-values arguments
                                                                """

<<<<<<< HEAD
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
=======
                                                                        if kwargs is not None and kwargs != {}:
                                                                                        for key in kwargs:
                                                                                                            if key == "created_at":
                                                                                                                                    self.__dict__["created_at"] = datetime.strptime(
                                                                                                                                                                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                                                    elif key == "updated_at":
                                                                                                                                                                            self.__dict__["updated_at"] = datetime.strptime(
                                                                                                                                                                                                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                                                                                                                                                                                            else:
                                                                                                                                                                                                                    self.__dict__[key] = kwargs[key]
                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                            self.id = str(uuid.uuid4())
                                                                                                                                                                                                                                                        self.created_at = datetime.now()
                                                                                                                                                                                                                                                                    self.updated_at = datetime.now()
                                                                                                                                                                                                                                                                                storage.new(self)
>>>>>>> b9e8b6ea79adec15c250701cc7608d7442baeb52

                                                                                                                                                                                                                                                                                    def __str__(self):
                                                                                                                                                                                                                                                                                                """Returns a human-readable string representation
                                                                                                                                                                                                                                                                                                        of an instance."""

<<<<<<< HEAD
    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.now()
=======
                                                                                                                                                                                                                                                                                                                return "[{}] ({}) {}".\
                                                                                                                                                                                                                                                                                                                                    format(type(self).__name__, self.id, self.__dict__)
>>>>>>> b9e8b6ea79adec15c250701cc7608d7442baeb52

                                                                                                                                                                                                                                                                                                                                        def save(self):
                                                                                                                                                                                                                                                                                                                                                    """Updates the updated_at attribute
                                                                                                                                                                                                                                                                                                                                                            with the current datetime."""

                                                                                                                                                                                                                                                                                                                                                                    self.updated_at = datetime.now()
                                                                                                                                                                                                                                                                                                                                                                            storage.save()

                                                                                                                                                                                                                                                                                                                                                                                def to_dict(self):
                                                                                                                                                                                                                                                                                                                                                                                            """Returns a dictionary representation of an instance."""

                                                                                                                                                                                                                                                                                                                                                                                                    my_dict = self.__dict__.copy()
                                                                                                                                                                                                                                                                                                                                                                                                            my_dict["__class__"] = type(self).__name__
                                                                                                                                                                                                                                                                                                                                                                                                                    my_dict["created_at"] = my_dict["created_at"].isoformat()
                                                                                                                                                                                                                                                                                                                                                                                                                            my_dict["updated_at"] = my_dict["updated_at"].isoformat()
                                                                                                                                                                                                                                                                                                                                                                                                                                    return my_dict
