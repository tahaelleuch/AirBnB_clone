#!/usr/bin/python3
"""
tests pour la classe city
"""
import unittest
from models.city import City
import models


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_City(self):
        """ tests des attribut"""
        instan = City()
        self.assertTrue(isinstance(instan, City))

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(City().id))
