"""
This module contains functions for calculating factorial,
and also check strong Number
"""
import math


def calculate_factorial(input_number):
    """
    Calculate the factorial of a number.

    Args:
        input_number (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of the input number.
    """
    if input_number == 0:
        return 1
    return input_number * calculate_factorial(input_number - 1)


def check_strong(input_num):
    """checking if the number is strong

    Args:
        input_num (int): the number to check weather it is
        strong number or not.

    Returns:
        str: Strong Number or Not Strong Number.
    """
    copy_input = input_num
    strong_num = 0
    while input_num != 0:
        remainder = input_num % 10
        strong_num = strong_num + math.factorial(remainder)
        input_num = input_num // 10
    if copy_input == strong_num:
        return "Strong Number"
    return "Not Strong Number"
