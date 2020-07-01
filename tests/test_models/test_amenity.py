#!/usr/bin/python3
"""
test pour la classe amenity
"""
import unittest
from models.amenity import Amenity
import models


class testAmenity(unittest.TestCase):
    """ test de classe"""

    def test_amenity(self):
        """ test des attribut"""
        instan = Amenity()
        self.assertTrue(isinstance(instan, Amenity))

    def test_unicite(self):
        """ test d unicité"""
        amn = Amenity()
        amn2 = Amenity()
        self.assertNotEqual(amn.id, amn2.id)

    def test_str_id(self):
        """ test de type de id en classe public"""
        self.assertEqual(str, type(Amenity().id))
