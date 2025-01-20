

class StringCalculator:

    def add(self, string_numbers: str)->int:
        """
        add method to return sum of numbers given as a single string
        """
        if not string_numbers:
            return 0

        """
        Split string of numbers by commas and convert each value to an integer and store them in a list.
        Sum the list of numbers.
        """
        sum_of_numbers = sum([int(num) for num in string_numbers.split(",")])
        return sum_of_numbers