"""
F_n = F_n-1 + F_n-2

Write a function F(n) that returns the nth Fibonacci number (0 indexed).
F(0) = 0 and F(1) = 1

0, 1, 2, 3, 4, 5, 6,  7,  8,  9
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""


def F(n):
    if n <= 1:
        return n

    return F(n - 1) + F(n - 2)


print(F(9))
