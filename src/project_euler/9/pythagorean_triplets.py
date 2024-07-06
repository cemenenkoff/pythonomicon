# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:12:21 2018

@author: Cemenenkoff

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def PE9():
    for a in range(1, 332):  # 332 + 333 + 335 = 1000; 332 = floor(1000/3)-1
        for b in range(a + 1, 499):  # 1 + 499 + 500 = 1000; 499 = floor(1000/2)-1
            if 2000 * (a + b) == 1000000 + 2 * a * b:
                c = 1000 - (a + b)
                if a**2 + b**2 == c**2:
                    return a * b * c


import timeit

start = timeit.default_timer()
answer = PE9()  # 31875000 found in 0.008162737881775683 seconds
elapsed = timeit.default_timer() - start
print("%s found in %s seconds" % (answer, elapsed))

"""
I broke this problem down by reducing the conditions:
    1. a<b<c
    2. a**2=b**2 = c**2
    3. a+b+c = 1000
to:
    1*. b>a
    2*. 2000*(a+b)= 1000000 + 2*a*b
by substituting c = 1000 - (a+b) into a**2+b**2=c**2 and then adding 2*a*b to
both sides to eliminate the (a+b)**2 terms.
"""
