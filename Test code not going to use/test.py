from django.test import TestCase

from app.calc import add

from app.calc import sub


class CalcTest(TestCase):

    def test_add_number(self):
        """Test two number"""
        self.assertEqual(add(3,8),11)

    def test_sub_number(self):
        "Test to check value of subtract"
        self.assertEqual(sub(12,11),1)