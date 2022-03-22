"""Tests for studyspace app models"""
from django.test import TestCase
from .models import Space, Reservation


class TestSpace(TestCase):
    """Tests for Space model"""
    def test_method(self):
        """Test for method"""
        self.assertEqual(1, 1)
