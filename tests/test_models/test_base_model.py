#!/usr/bin/python3
"""Unit tests for the BaseModel class. """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time # Import time module to create delays for testing updated_at
import uuid

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_instance_creation(self):
        """Test that a BaseModel instance is created correctly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)
        self.assertEqual(obj.created_at, obj.updated_at)

    def test_unique_ids(self):
        """Test that each BaseModel instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_save_method(self):
        """Test that the save method updates the updated_at attribute."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        time.sleep(0.01)  # Ensure time difference
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test that the to_dict method returns a correct dictionary representation."""
        obj = BaseModel()
        obj.name = "Test"
        obj.number = 42
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['name'], "Test")
        self.assertEqual(obj_dict['number'], 42)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

        # Check ISO format of datetime strings
        try:
            datetime.fromisoformat(obj_dict['created_at'])
            datetime.fromisoformat(obj_dict['updated_at'])
        except ValueError:
            self.fail("created_at or updated_at is not in ISO format")