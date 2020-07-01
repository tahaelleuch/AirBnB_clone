#!/usr/bin/python3
"""
tests pour la classe state
"""
import unittest
from models.state import State
from datetime import datetime


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_Place(self):
        """ tests des attribut"""
        instan = State()
        self.assertTrue(isinstance(instan, State))

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(State().id))

    def test_str_name(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(State().name))

    def test_date_creation(self):
        """ verification date de creation"""
        self.assertEqual(datetime, type(State().created_at))
