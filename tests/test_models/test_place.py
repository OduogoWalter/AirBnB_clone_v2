#!/usr/bin/python3
"""Unit tests for Place model"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for Place model"""

    def setUp(self):
        """Set up test environment"""
        self.place = Place()

    def test_city_id_type(self):
        """Test type of city_id attribute"""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_type(self):
        """Test type of user_id attribute"""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_type(self):
        """Test type of name attribute"""
        self.assertIsInstance(self.place.name, str)

    def test_description_type(self):
        """Test type of description attribute"""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_type(self):
        """Test type of number_rooms attribute"""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Test type of number_bathrooms attribute"""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_type(self):
        """Test type of max_guest attribute"""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_type(self):
        """Test type of price_by_night attribute"""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_type(self):
        """Test type of latitude attribute"""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_type(self):
        """Test type of longitude attribute"""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_type(self):
        """Test type of amenity_ids attribute"""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == "__main__":
    unittest.main()
