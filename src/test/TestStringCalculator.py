import unittest
from StringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    """ 
    Test cases for StringCalculator class.
    """
    def setUp(self):
        """
        Setup method to create an instance of StringCalculator before each test.
        """
        self.calculator = StringCalculator()

    def test_add_empty_string(self):
        """
        Test that an empty string returns 0.
        Input: ""
        Expected Output: 0
        """
        result = self.calculator.add("")
        self.assertEqual(result, 0)

    def test_add_single_number(self):
        """
        Test for single number to return the same number
        Input: "3"
        Expected Output: 3
        """
        result = self.calculator.add("3")
        self.assertEqual(result, 3)

    def test_add_two_numbers(self):
        """
        Test for two numbers to return the sum of two numbers
        Input: "3,7"
        Expected Output: 10
        """
        result = self.calculator.add("3,7")
        self.assertEqual(result, 10)

    def test_add_multiple_numbers(self):
        """
        Test for multiple numbers to return the sum of all the numbers
        Input: "1,2,3,4,5,6,7,8,9,10"
        Expected Output: 55
        """
        result = self.calculator.add("1,2,3,4,5,6,7,8,9,10")
        self.assertEqual(result, 55)

    def test_add_newlines_between_numbers(self):
        """
        Test for allowing add method to handle newlines between numbers
        Input: "1\n2\n3,4,10"
        Expected Ouput: 20
        """
        result = self.calculator.add("1\n2\n3,4,10")
        self.assertEqual(result, 20)

    def test_add_change_of_delimiter(self):
        """
        Test for allowing add method to handle change of default delimiter between numbers
        Input: "//;\n1;2;3;4;10"
        Expected Output: 20
        """
        result = self.calculator.add("//;\n1;2;3;4;10")
        self.assertEqual(result, 20)

    def test_add_for_negative_numbers(self):
        """
        Test for add method to raise an exception with a message when passed with a negative number
        Input: "1,2,-3,4,-10"
        Expected Output: "negative numbers not allowed: -3, -10"
        """
        with self.assertRaises(ValueError) as error:
            self.calculator.add("1,2,-3,4,-10")
        
        exception_msg = str(error.exception)
        self.assertEqual(exception_msg, "negative numbers not allowed: -3, -10")

    def test_GetCalledCount(self):
        """
        Test for GetCalledCount to return number of times the add method is invoked
        Input: multiple add calls
        Expected Output: 3 (add() is being called for 3 times)
        """
        self.calculator.add("3,4")
        self.calculator.add("3,4,10")
        self.calculator.add("1\n2\n3,4")
        result = self.calculator.GetCalledCount()
        self.assertEqual(result, 3)

    def test_add_ignore_numbers_greater_than_1000(self):
        """
        Test for add method to ignore numbers greater than 1000 and sum the remaining numbers
        Input: "1,2,3,1001,10,1020,20"
        Expected Output: 36
        """
        result = self.calculator.add("1,2,3,1001,10,1020,20")
        self.assertEqual(result, 36)

    def test_add_delimiter_of_any_length(self):
        """
        Test for add method to handle delimiter of any length with format "//[***]\n1***2***3"
        Input: "//[***]\n1***2***3***4***10"
        Expected Output: 20
        """
        result = self.calculator.add("//[***]\n1***2***3***4***10")
        self.assertEqual(result, 20)

    def test_add_multiple_delimiter(self):
        """
        Test for add method to handle mutliple delimiters with format "//[*][%]\n1*2%3"
        Input: "//[*][%]\n1*2%3*4%10"
        Expected Output: 20
        """
        result = self.calculator.add("//[*][%]\n1*2%3*4%10")
        self.assertEqual(result, 20)

    def test_add_multiple_delimiter_of_any_length(self):
        """
        Test for add method to handle multiple delimiters of any length with format "//[**][%%]\n1**2%%3"
        Input: "//[**][%%]\n1**2%%3**4%%10"
        Expected Output: 20
        """
        result = self.calculator.add("//[**][%%]\n1**2%%3**4%%10")
        self.assertEqual(result, 20)