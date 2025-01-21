import re

class StringCalculator:
    """
    A class that implements a string calculator to add numbers from a given string of numbers.
    It allows for newlines between numbers, change of delimiters, multiple delimiters of any length.

    It implements two methods: add(), GetCalledCount()

    Attributes:
    Count(int): The count of how many times the add() method was invoked.
    """
    def __init__(self):
        """
        Initiliazes a StringCalculator instance with count attribute and sets that to 0.
        """
        self.count = 0

    def add(self, string_numbers: str)->int:
        """
        add method that sums the numbers from a given string and allows for custom delimiters, newline between 
        numbers, multiple delimiters, ignoring numbers > 1000 and raises an exception for negative numbers

        Parameters:
        string_numbers(str): string of numbers with custom delimiters, newline between numbers or commas
        it supports the following formats in the input string:
        1. comma seperated values: "1,2,3,4"
        2. Newline between numbers: "1\n2\n3,4"
        3. Customer delimiters: "//[delimiter]\n[numbers..]"

        Returns:
        int: The sum of the numbers in the given string

        Raises:
        ValueError: Raises a ValueError for negative numbers in the input string with a message 
        "negatives not allowed" followed by the negative numbers

        """
        # return 0 for empty string
        if not string_numbers:
            self.count+=1
            return 0

        """
        Change of delimiter has a pattern of "//[delimiter]\n1[numbers..]"
        For ex: “//;\n1;2” == 3.
        Check if given string starts with "//" and find first newline character index to seperate numbers
        and delimiter."
        """
        if string_numbers.startswith("//"):
            newline_index = string_numbers.index("\n")
            delimiter_substring = string_numbers[2:newline_index]

            string_numbers = string_numbers[newline_index+1:]

            if delimiter_substring.startswith("["):
                delimiters = re.findall(r'\[([^\]]+)\]', delimiter_substring)
                for delimiter in delimiters:
                    string_numbers = string_numbers.replace(delimiter, ",")
            else:
                string_numbers = string_numbers.replace(delimiter_substring, ",")

        # replace newline character ("\n") with "," between numbers
        string_numbers = string_numbers.replace("\n", ",")

        # check for negative numbers
        negative_numbers = []
        for num in string_numbers.split(","):
            if int(num) < 0:
                negative_numbers.append(num)
            else:
                continue

        if len(negative_numbers) > 0:
            self.count+=1
            raise ValueError(f"negative numbers not allowed: {', '.join(negative_numbers)}")

        """
        Split string of numbers by commas and convert each value to an integer and store them in a list.
        Sum the list of numbers ignoring numbers > 1000 by replacing them with 0
        """
        sum_of_numbers = sum([0 if int(num) > 1000 else int(num) for num in string_numbers.split(",")])
        self.count+=1
        return sum_of_numbers
    
    def GetCalledCount(self)->int:
        """
        Parameters: None
        
        Returns:
        int: The count of number of times the add() method was called
        """
        return self.count