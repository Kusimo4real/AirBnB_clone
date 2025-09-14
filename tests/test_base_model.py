import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def test_instance_creation(self):
        """Test that an instance of BaseModel is created correctly."""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_id(self):
        """Test that each instance has a unique id."""
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)
        self.assertTrue(uuid.UUID(obj1.id))
        self.assertTrue(uuid.UUID(obj2.id))
    
    def test_str_representation(self):
        """Test the string representation of the BaseModel instance."""
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        """Test that the save method updates the updated_at attribute."""
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)
        self.assertGreater(obj.updated_at, old_updated_at)

    def test_to_dict_method(self):
        """Test that the to_dict method returns a correct dictionary representation."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())
        

    def test_to_dict_contains_correct_keys(self):
        """Test that the_to_dict method contains all necessary keys."""
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()