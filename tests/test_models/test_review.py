#!/usr/bin/python3
"""
tests pour la classe state
"""
import unittest
from models.review import Review
import models
from datetime import datetime


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_Place(self):
        """ tests des attribut"""
        instan = Review()
        self.assertTrue(isinstance(instan, Review))

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Review().place_id))

    def test_str_user(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Review().user_id))

    def test_text_str(self):
        """ verification text de creation"""
        self.assertEqual(str, type(Review().text))
