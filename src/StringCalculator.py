

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
        list_of_numbers = [int(num) for num in string_numbers.split(",")]
        sum_of_numbers = sum(list_of_numbers)
        return sum_of_numbers