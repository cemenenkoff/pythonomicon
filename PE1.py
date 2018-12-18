# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:34:27 2018

@author: Cemenenkoff

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

tot=0
for num in range(1000):
    if num%3==0 or num%5==0:
        tot = tot + num

#Now we make a function so we can time our answer.
def PE1():
    tot=0
    for num in range(1000):
        if num%3==0 or num%5==0:
            tot = tot + num
    return tot

import time
start = time.time()
answer = PE1()
elapsed = (time.time() - start)
print ('%s found in %s seconds' % (answer, elapsed))