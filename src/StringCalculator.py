

class StringCalculator:

    def add(self, string_numbers: str)->int:
        """
        add method to return sum of numbers given input of string of numbers
        """
        # return 0 for empty string
        if not string_numbers:
            return 0

        """
        Change of delimiter has a pattern of "//[delimiter]\n1[numbers..]"
        For ex: “//;\n1;2” == 3.
        Check if given string starts with "//" and find first newline character index to seperate numbers
        and delimiter."
        """
        if string_numbers.startswith("//"):
            newline_index = string_numbers.index("\n")
            delimiter = string_numbers[newline_index-1]
            string_numbers = string_numbers[newline_index+1:]
            string_numbers = string_numbers.replace(delimiter, ",")

        # replace newline character ("\n") with "," between numbers
        string_numbers = string_numbers.replace("\n", ",")

        negative_numbers = []
        for num in string_numbers.split(","):
            if int(num) < 0:
                negative_numbers.append(str(num))
            else:
                continue

        if len(negative_numbers) > 0:
            raise ValueError(f"negative numbers not allowed: {', '.join(negative_numbers)}")

        """
        Split string of numbers by commas and convert each value to an integer and store them in a list.
        Sum the list of numbers.
        """
        sum_of_numbers = sum([int(num) for num in string_numbers.split(",")])
        return sum_of_numbers