#!/usr/bin/python3
import datetime
import unittest
import uuid
import models
from models.base_model import BaseModel
"""
testeur pour la classe BaseModel
"""


class testbase(unittest.TestCase):
    def test_attributes(self):
    base1 = BaseModel()
    base2 = BaseModel()
    self.assertTrue(isinstance(base1, BaseModel))
    self.assertEqual(str, type(BaseModel().id))
    self.assertNotEqual(base1.id, base2.id)
    self.assertTrue(isinstance(base1.created_at, datetime))
    self.assertTrue(isinstance(base2.updated_at, datetime))
    base1.name = "test"
    self.assertEqual(base1.name, "test")
    self.assertTrue(type(base1.to_dict()), dict)
