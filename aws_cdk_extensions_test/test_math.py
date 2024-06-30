from aws_cdk_extensions.math_operation.math_operations import MathOperations

def test_add():
    assert MathOperations.add(1, 2) == 3
    assert MathOperations.add(-1, 1) == 0
    assert MathOperations.add(-1, -1) == -2

def test_subtract():
    assert MathOperations.subtract(2, 1) == 1
    assert MathOperations.subtract(2, 3) == -1
    assert MathOperations.subtract(-1, -1) == 0

def test_multiply():
    assert MathOperations.multiply(2, 3) == 6
    assert MathOperations.multiply(-1, 1) == -1
    assert MathOperations.multiply(-1, -1) == 1

def test_divide():
    assert MathOperations.divide(6, 2) == 3
    assert MathOperations.divide(-6, 2) == -3
    assert MathOperations.divide(-6, -2) == 3
    try:
        MathOperations.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
