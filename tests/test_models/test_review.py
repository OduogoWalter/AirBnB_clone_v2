#!/usr/bin/python3
"""Unit tests for Review model"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for Review model"""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def test_place_id_type(self):
        """Test type of place_id attribute"""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_type(self):
        """Test type of user_id attribute"""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_type(self):
        """Test type of text attribute"""
        self.assertIsInstance(self.review.text, str)
