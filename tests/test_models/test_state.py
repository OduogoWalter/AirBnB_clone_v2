#!/usr/bin/python3
"""Unit tests for State model"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State model"""

    def setUp(self):
        """Set up test environment"""
        self.state = State()

    def test_name_type(self):
        """Test type of name attribute"""
        self.assertIsInstance(self.state.name, str)
