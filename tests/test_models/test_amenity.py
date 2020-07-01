#!/usr/bin/python3
"""
tests pour la classe amenity
"""
import unittest
from models.amenity import Amenity
import models


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_amenity(self):
        """ tests des attribut"""
        instan = Amenity()
        self.assertTrue(isinstance(instan, Amenity))

    def test_unicite(self):
        """ tests d unicité"""
        amn = Amenity()
        amn2 = Amenity()
        self.assertNotEqual(amn.id, amn2.id)

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Amenity().id))

    def test_str_name(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Amenity().name))
