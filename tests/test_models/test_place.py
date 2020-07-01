#!/usr/bin/python3
"""
tests pour la classe place
"""
import unittest
from models.place import Place


class testAmenity(unittest.TestCase):
    """ tests de classe"""

    def test_Place(self):
        """ tests des attribut"""
        instan = Place()
        self.assertTrue(isinstance(instan, Place))

    def test_str_cityid(self):
        """ tests de type de cityid en classe public"""
        self.assertEqual(str, type(Place().city_id))

    def test_str_userid(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Place().user_id))

    def test_str_desc(self):
        """ tests de type de id en classe public"""
        self.assertEqual(str, type(Place().description))

    def test_nbr_chambtr(self):
        """ tests de type de id en classe public"""
        self.assertEqual(int, type(Place().number_rooms))

    def test_nbr_sdb(self):
        """ tests de type de id en classe public"""
        self.assertEqual(int, type(Place().number_bathrooms))

    def test_nbr_invite(self):
        """ tests de type de id en classe public"""
        self.assertEqual(int, type(Place().max_guest))

    def test_prix(self):
        """ tests de type de id en classe public"""
        self.assertEqual(int, type(Place().price_by_night))

    def test_amn(self):
        """ tests de type de id en classe public"""
        self.assertEqual(list, type(Place().amenity_ids))

    def test_orientation(self):
        """ tests de type de id en classe public"""
        self.assertEqual(float, type(Place().latitude))
        self.assertEqual(float, type(Place().longitude))
