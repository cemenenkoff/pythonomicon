# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:43:18 2018

@author: Cemenenkoff

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""
def PE6():
    tot=0 #Running sum of the square of each natural number below 100.
    sumnat_sq = (50*101)**2 #Sum of the natural numbers below 100, squared.
    for num in range(1,100+1):
        tot=num**2+tot
    return int(sumnat_sq-tot)

import timeit
start = timeit.default_timer()
answer = PE6() #25164150 found in 2.8281859941890533e-05 seconds
elapsed = (timeit.default_timer() - start)
print ('%s found in %s seconds' % (answer, elapsed))