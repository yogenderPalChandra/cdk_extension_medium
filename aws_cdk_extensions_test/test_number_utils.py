# test_file_utils.py

import os
# from file_utils import NumberUtils
from aws_cdk_extensions.number_utils.number_utils import NumberUtils

def test_is_prime():
    assert NumberUtils.is_prime(2) is True
    assert NumberUtils.is_prime(4) is False
    assert NumberUtils.is_prime(7) is True
    assert NumberUtils.is_prime(9) is False

def test_fibonacci():
    assert NumberUtils.fibonacci(1) == 1
    assert NumberUtils.fibonacci(5) == 5
    assert NumberUtils.fibonacci(10) == 55
    try:
        NumberUtils.fibonacci(0)
    except ValueError as e:
        assert str(e) == "Input must be a positive integer"

def test_factorial():
    assert NumberUtils.factorial(0) == 1
    assert NumberUtils.factorial(3) == 6
    assert NumberUtils.factorial(5) == 120
    try:
        NumberUtils.factorial(-1)
    except ValueError as e:
        assert str(e) == "Input must be a non-negative integer"

