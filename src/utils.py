import timeit
from typing import Callable


def timer(func: Callable):
    """Print the execution time of a function.

    This function is intended to be used as a decorator to measure the time
    a function takes to execute. It prints the result of the function and the
    elapsed time in seconds.

    Args:
        func (Callable): The function to be timed.

    Returns:
        Callable: A wrapper function that executes the input function and
            prints its execution time.
    """

    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        elapsed = timeit.default_timer() - start
        print(f"{func.__name__: >40}: {result} found in {elapsed} seconds")
        return result

    return wrapper
