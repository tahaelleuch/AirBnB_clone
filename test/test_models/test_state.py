#!/usr/bin/python3
"""
test pour la classe state
"""
import unittest
from models.state import state
import models
from datetime import datetime


class testAmenity(unittest.TestCase):
    """ test de classe"""

    def test_Place(self):
        """ test des attribut"""
        instan = state()
        self.assertTrue(isinstance(instan, state))

    def test_str_id(self):
        """ test de type de id en classe public"""
        self.assertEqual(str, type(state().id))

    def test_date_creation(self):
        """ verification date de creation"""
        self.assertEqual(datetime, type(State().created_at))
