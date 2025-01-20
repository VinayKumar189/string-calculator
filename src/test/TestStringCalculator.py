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

    def test_add_single_number(self):
        """
        Test for single number returns as is
        """
        result = self.calculator.add("3")
        self.assertEqual(result, 3)

    def test_add_two_numbers(self):
        """
        Test for single number returns as is
        """
        result = self.calculator.add("3,7")
        self.assertEqual(result, 10)

    def test_add_multiple_numbers(self):
        """
        Test for single number returns as is
        """
        result = self.calculator.add("1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(result, 55)

    