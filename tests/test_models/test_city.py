#!/usr/bin/python3
"""
test pour la classe city
"""
import unittest
from models.city import City
import models


class testAmenity(unittest.TestCase):
    """ test de classe"""

    def test_City(self):
        """ test des attribut"""
        instan = City()
        self.assertTrue(isinstance(instan, City))

    def test_str_id(self):
        """ test de type de id en classe public"""
        self.assertEqual(str, type(City().id))
