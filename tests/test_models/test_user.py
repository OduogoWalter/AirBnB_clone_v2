#!/usr/bin/python3
"""Unit tests for User model"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User model"""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def test_first_name_type(self):
        """Test type of first_name attribute"""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_type(self):
        """Test type of last_name attribute"""
        self.assertIsInstance(self.user.last_name, str)

    def test_email_type(self):
        """Test type of email attribute"""
        self.assertIsInstance(self.user.email, str)

    def test_password_type(self):
        """Test type of password attribute"""
        self.assertIsInstance(self.user.password, str)


if __name__ == "__main__":
    unittest.main()
