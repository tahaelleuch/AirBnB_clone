#!/usr/bin/python3
"""
tests pour la classe state
"""
import unittest
from models.user import User
import models
from datetime import datetime


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_Place(self):
        """ tests des attribut"""
        instan = User()
        self.assertTrue(isinstance(instan, User))

    def test_str_id(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(User().id))

    def test_unicite_id(self):
        """ tests unicité"""
        admin1 = User()
        admin2 = User()
        self.assertNotEqual(admin2.id, admin1.id)

    def test_email(self):
        """ tests type de mail """
        self.assertEqual(str, type(User.email))

    def test_pswd(self):
        """ tests type de mail """
        self.assertEqual(str, type(User.password))

    def test_nom_user(self):
        """ tests type de mail """
        self.assertEqual(str, type(User.first_name))

    def test_prenom_user(self):
        """ tests type de mail """
        self.assertEqual(str, type(User.last_name))

    def test_date_creation(self):
        """ verification date de creation"""
        self.assertEqual(datetime, type(User().created_at))
