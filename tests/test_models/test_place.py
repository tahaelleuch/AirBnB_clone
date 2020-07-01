#!/usr/bin/python3
"""
tests pour la classe place
"""
import unittest
from models.place import Place
import models


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_Place(self):
        """ tests des attribut"""
        instan = Place()
        self.assertTrue(isinstance(instan, BaseModel))

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Place().id))
