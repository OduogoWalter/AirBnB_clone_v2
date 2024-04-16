#!/usr/bin/python3
"""Unit tests for City model"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City model"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def test_state_id_type(self):
        """Test type of state_id attribute"""
        self.assertIsInstance(self.city.state_id, str)

    def test_name_type(self):
        """Test type of name attribute"""
        self.assertIsInstance(self.city.name, str)
