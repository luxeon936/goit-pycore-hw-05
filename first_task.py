from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    """
    Caching function to calculate fibonacci sequence

    Calls:
        fibonacci function
    """
    cache = {0:0, 1:1}
    def fibonacci(n:int) -> int:
        """
        Function to calculate fibonacci number

        Returns:
            Fibonacci number at n-th place
        """
        if type(n) != int:
            raise TypeError("Input not an integer")
        if n < 0:
            raise ValueError("Input must be a positive integer")
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci
