# Question 1

# Write a function that prints "Fizz" when the number is divisible by 3, "Buzz" when the number is divisible by 5
# and "FizzBuzz" when the number is divisible by both 3 and 5.
# If the number is not divisible by either 3 or 5, the function should return the number itself.


def fizz_buzz(number):
    """Returns Fizz if number is divisible by 3, Buzz if divisible by 5, FizzBuzz if divisible by both 3 and 5.
    If not divisible by either 3 or 5, returns the number itself.
    >>> fizz_buzz(3)
    'Fizz'
    >>> fizz_buzz(5)
    'Buzz'
    >>> fizz_buzz(15)
    'FizzBuzz'
    """
    if isinstance(number, int) and number >= 0:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        else:
            return number
    return


# Question 2

# Write a function that takes a list of numbers and returns the sum of the squares of all the numbers.


def sum_of_squares(numbers):
    """Returns the sum of the squares of all the numbers in a list.
    >>> sum_of_squares([1, 2, 3])
    14
    >>> sum_of_squares([2, 4, 6])
    56
    """
    if isinstance(numbers, list) and all(isinstance(n, (int, float)) for n in numbers):
        return sum(n ** 2 for n in numbers)
    return


# Question 3

# Write a function that counts the number of vowels in a string.


def count_vowels(string):
    """Returns the number of vowels in a string.
    >>> count_vowels("hello")
    2
    >>> count_vowels("aeiou")
    5
    """
    if isinstance(string, str): 
        vowels = "aeiou"
        string = string.lower()
        # Count vowels in the string"
        return sum(1 for char in string if char in vowels)
    return


# Question 4

# Write a function that counts the number of repeated characters in a string.


def count_repeats(string):
    """Returns the number of repeated characters in a string.
    >>> count_repeats("hello")
    2
    >>> count_repeats("aeiou")
    0
    """
    if isinstance(string, str):
       repeated_chars = 0
       checked_chars = []

       for char in string:
            # first occurance of a character
            if char not in checked_chars:
                count  = string.count(char)
                if count > 1:
                    repeated_chars+=count
                checked_chars.append(char)
       return repeated_chars
    return

        
       
    

if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
