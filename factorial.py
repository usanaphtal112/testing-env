"""
This module contains functions for calculating factorial.
"""


def calculate_factorial(input_number):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.
    """
    if input_number == 0:
        return 1
    return input_number * calculate_factorial(input_number - 1)
