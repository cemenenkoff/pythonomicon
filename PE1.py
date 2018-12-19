# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 12:34:27 2018

@author: Cemenenkoff

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def PE1():
    tot=0
    for num in range(1000):
        if num%3==0 or num%5==0:
            tot = tot + num
    return tot

import math
def PE1_math(a,b,n):
    if b<a:
        a,b=b,a #Tuple swap: b>a now.
        """Python evaluates expressions from left to right, but when evaluating
        an assignment, the right-hand side is evaluated before the left-hand
        side. Then the first LHS identifier (a) is assigned to the first
        element of the RHS tuple, and the second LHS identifier (b) assigned to
        the second element of the RHS tuple."""
    la = math.ceil(n/a)-1 #ceil and -1 in case a divides n.
    lb = math.ceil(n/b)-1 #lb stands for "last b multiple", etc.
    lc = int(lb/a) #It's ok for a to divide lb, so just truncate it.
    return a*la/2*(la+1)+b*lb/2*(lb+1)-a*b*lc/2*(lc+1)

import timeit #Better than the time module to find speeds of solutions.
start = timeit.default_timer()
#answer = PE1() #233168 found in 0.0001084950661563904 seconds
answer = PE1_math(3,5,1000) #233168.0 found in 7.801892024872359e-06 seconds
elapsed = (timeit.default_timer() - start)
print ('%s found in %s seconds' % (answer, elapsed))

"""
I approached this problem by thinking about sorting, but also by using basic
number theory. Each approach had a relatively simple solution, but it turns out
that  math wins at the end of the day (17 times faster!). My way of solving
this mathematically came from initially thinking about two summations:
            3i from i=1,...,333    and    5i from i=1,...,199.
The ending i for each series is found by thinking about which multiple is the
largest one strictly less than 1000: 3*333=999 and 199*5=995. Notice though
that we have overcounting occurring. We can think of this in two ways: the
double count occurs every 3rd term in the 5i series, or every 5th term in the
3i series. I chose the convention of eliminating terms from the larger factor's
series. The adjustment for b|n is made with lb which ensures lc's accuracy, so
in the end we use the sum of integers from 1 to n formula three times to get
the answer by direct calculation.
"""