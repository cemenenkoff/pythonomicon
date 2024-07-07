"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import math

if __name__ == "__main__":
    import sys
    from pathlib import Path

    parent_dir = Path(__file__).resolve().parents[2]
    sys.path.append(str(parent_dir))
    from utils import timer


@timer
def sum_of_multiples_below_n(a: int, b: int, n: int) -> int:
    """Sum all multiples of a or b below n, where a, b, and n are integers.

    Args:
        a (int): An integer less than n.
        b (int): An integer less than n, distinct from a.
        n (int): A integer greater than a and also greater than b.

    Returns:
        int: The sum of all multiples of a or b below n.
    """
    tot = 0
    for num in range(n):
        if num % a == 0 or num % b == 0:
            tot += num
    return tot


@timer
def sum_of_multiples_below_n_clever(a: int, b: int, n: int) -> int:
    """Sum all multiples of a or b below n without double-counting.

    Args:
        a (int): An integer less than n.
        b (int): An integer less than n, distinct from a.
        n (int): A integer greater than a and also greater than b.

    Returns:
        int: The sum of all multiples of a or b below n.
    """
    if b < a:
        a, b = b, a
    lai = round(math.ceil(n / a) - 1)  # `lai` stands for "last a index", etc.
    lbi = round(math.ceil(n / b) - 1)  # `ceil` and - 1 in case b divides n.
    lci = lbi // a  # It's ok for `a` to divide `lb`, so just truncate it.
    sum_of_a_multiples = a * lai / 2 * (lai + 1)
    sum_of_b_multiples = b * lbi / 2 * (lbi + 1)
    double_counts = a * b * lci / 2 * (lci + 1)
    return int(sum_of_a_multiples + sum_of_b_multiples - double_counts)


def main():
    """
    I approached this problem by thinking about sorting, but also by using basic number
    theory. Each approach had a relatively simple solution, but it turns out that number
    theory wins at the end of the day. My way of solving this mathematically came from
    initially thinking about two summations:
        3i for i in (1, ..., 333)
        5i for i in (1, ..., 199)

    The ending i for each series is found by thinking about which multiple is the
    largest one strictly less than 1000:
        3 * 333 = 999 and 199 * 5 = 995.

    Notice though, that we have overcounting occurring. We can think of this in two
    ways: the double count occurs every 3rd term in the 5i series, or every 5th term in
    the 3i series. I chose the convention of eliminating terms from the larger factor's
    series.
        15i for i in (1, ..., 66)

    The adjustment for b | n is made with `lbi` which ensures the accuracy of `lci`, so
    in the end we use the sum of integers from 1 to n formula three times to get the
    answer by direct calculation.
    """
    args = (3, 5, 1000)
    funcs = [sum_of_multiples_below_n, sum_of_multiples_below_n_clever]
    for func in funcs:
        func(*args)


if __name__ == "__main__":
    main()
