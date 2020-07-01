#!/usr/bin/python3
"""
test pour la classe place
"""
import unittest
from models.city import Place
import models


class testAmenity(unittest.TestCase):
    """ test de classe"""

    def test_Place(self):
        """ test des attribut"""
        instan = Place()
        self.assertTrue(isinstance(instan, BaseModel))

    def test_str_id(self):
        """ test de type de id en classe public"""
        self.assertEqual(str, type(Place().id))
