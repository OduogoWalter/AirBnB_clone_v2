#!/usr/bin/python3
"""Unit tests for Amenity model"""


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity model"""

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity()

    def test_name_type(self):
        """Test type of name attribute"""
        self.assertIsInstance(self.amenity.name, str)
