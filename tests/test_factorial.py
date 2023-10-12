"""
Unit tests for the calculate_factorial function in the factorial module.
"""
from factorial import calculate_factorial


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
