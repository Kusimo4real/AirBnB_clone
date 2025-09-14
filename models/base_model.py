#!/usr/bin/python3
"""Defines the BaseModel class for the AirBnB clone project.

This module contains the BaseModel class which defines all common
attributes and methods for other classes in the AirBnB clone project.
"""

from datetime import datetime
import uuid


class BaseModel:
    """Represents the BaseModel for all AirBnB clone models.

    This class defines all common attributes and methods for other classes.
    """

    def __init__(self):
        """Initializes a new BaseModel instance.

        Assigns a unique id, and sets created_at and updated_at to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns the string representation of the BaseModel instance.

        Format: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance.

        Includes a __class__ key with the class name, and converts
        created_at and updated_at to ISO format strings.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
