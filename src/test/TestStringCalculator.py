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
        Test for single number to return the same number
        """
        result = self.calculator.add("3")
        self.assertEqual(result, 3)

    def test_add_two_numbers(self):
        """
        Test for two numbers to return the sum
        """
        result = self.calculator.add("3,7")
        self.assertEqual(result, 10)

    def test_add_multiple_numbers(self):
        """
        Test for multiple numbers to return the sum of all the numbers
        """
        result = self.calculator.add("1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(result, 55)

    def test_add_newlines_between_numbers(self):
        """
        Test for allowing add method to handle newlines between numbers
        """
        result = self.calculator.add("1\n2\n3,4,10")
        self.assertEqual(result, 20)

    def test_add_change_of_delimiter(self):
        """
        Test for allowing add method to handle change of default delimiter between numbers
        """
        result = self.calculator.add("//;\n1;2;3;4;10")
        self.assertEqual(result, 20)

    def test_add_for_negative_numbers(self):
        """
        Test for add method to raise an exception with a message "negative numbers not allowed <negative number>"
        when passed with a negative number
        """
        with self.assertRaises(ValueError) as error:
            self.calculator.add("1,2,-3,4,-10")
        
        exception_msg = str(error.exception)
        self.assertEqual(exception_msg, "negative numbers not allowed: -3, -10")

    def test_GetCalledCount(self):
        call_1 = self.calculator.add("3,4")
        call_2 = self.calculator.add("3,4,10")
        result = self.calculator.GetCalledCount()
        self.assertEqual(result, 2)
    