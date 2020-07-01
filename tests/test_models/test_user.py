#!/usr/bin/python3
"""
test pour la classe state
"""
import unittest
from models.user import User
import models
from datetime import datetime


class testAmenity(unittest.TestCase):
    """ test de classe"""

    def test_Place(self):
        """ test des attribut"""
        instan = User()
        self.assertTrue(isinstance(instan, User))

    def test_str_id(self):
        """ test de type de id en classe public"""
        self.assertEqual(str, type(User().id))

    def test_unicite_id(self):
        """ test unicité"""
        admin1 = User()
        admin2 = User()
        self.assertNotEqual(admin2.id, admin1.id)

    def test_email(self):
        """ test type de mail """
        self.assertEqual(str, type(User.email))

    def test_date_creation(self):
        """ verification date de creation"""
        self.assertEqual(datetime, type(User().created_at))
