"""
Unit tests for the calculate_factorial function in the factorial module.
"""
from factorial import calculate_factorial, check_strong


def test_factorial():
    """
    Test the calculate_factorial function.

    This function includes multiple test cases to check if the
    calculate_factorial function computes factorials correctly.
    """
    assert calculate_factorial(0) == 1
    assert calculate_factorial(1) == 1
    assert calculate_factorial(5) == 120
    assert calculate_factorial(10) == 3628800


def test_strong():
    """Test the function that is checking
    weather the number is strong or not
    """

    assert check_strong(145) == "Strong Number"
    assert check_strong(122) == "Not Strong Number"
    assert check_strong(1) == "Strong Number"
    assert check_strong(40585) == "Strong Number"
    assert check_strong(100000) == "Not Strong Number"
    assert check_strong(0) == "Strong Number"
