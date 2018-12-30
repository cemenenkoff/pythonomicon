# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 09:47:56 2018

@author: Cemenenkoff

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np
def is_prime(n):
    if n%2==0: #Return False if the number is even.
        return False
    else: #Instead, if the number is odd:
        for possible_factor in range(3, int(np.sqrt(n))+1, 2):#*1
            if n%possible_factor==0:
                return False
        return True
#*1: Notice we skip by 2 to only check odd numbers. The +1 is added for the
#case of 9 to avoid range(3,3). The ceiling of sqrt(n) comes from the fact that
#for nonzero a, b, and n, where b!=n and a!=n, 
#if n = ab, then n is composite.
#if a>sqrt(n) and b>sqrt(n), then ab>sqrt(n), so by the contrapositive,
#if ab<=sqrt(n), then a<=sqrt(n) or b<=sqrt(n).

#tqdm enables a progress bar for for loops by wrapping tqdm() around range().
from tqdm import tqdm
def PE10():
    tot = 2
    for num in tqdm(range(3,2*10**6,2)):
        if is_prime(num) == True:
            tot+=num
    return tot

import timeit
start = timeit.default_timer()
answer = PE10() #142913828922 found in 6.996392108865621 seconds
elapsed = (timeit.default_timer() - start)
print('%s found in %s seconds'%(answer, elapsed))