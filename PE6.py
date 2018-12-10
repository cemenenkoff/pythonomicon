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
    sum_nat = lambda n: (n/2)*(n+1)
    tot=0
    for number in range(1,100+1):
        tot=number**2+tot
    return int(sum_nat(100)**2-tot)

import time
start = time.time()
answer = PE6()
elapsed = (time.time() - start)
print ('%s found in %s seconds' % (answer, elapsed))
#25164150 found in 0.0 seconds