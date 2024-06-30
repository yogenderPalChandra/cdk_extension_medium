# number_utils.py

class NumberUtils:

    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if a number is a prime number."""
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def fibonacci(n: int) -> int:
        """Return the nth Fibonacci number."""
        if n <= 0:
            raise ValueError("Input must be a positive integer")
        a, b = 0, 1
        for _ in range(n-1):
            a, b = b, a + b
        return b

    @staticmethod
    def factorial(n: int) -> int:
        """Return the factorial of a number."""
        if n < 0:
            raise ValueError("Input must be a non-negative integer")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
