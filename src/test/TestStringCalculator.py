import unittest
from StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        """
        Setup method to create an instance of StringCalculator before each test.
        """
        self.calculator = StringCalculator()

    def test_add_empty_string(self):
        """
        Test that an empty string returns 0.
        """
        result = self.calculator.add("")
        self.assertEqual(result, 0)