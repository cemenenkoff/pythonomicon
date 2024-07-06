# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 05:32:59 2019

@author: Cemenenkoff

I pretty much only used math for this solution. Since scipy already has an
efficient choose function, I employed it here.

On the 20x20 grid, if we start in the upper left and end in the bottom right,
only moving down or up, we must have exactly 20 down moves and 20 right moves
for every possible pathway (2n choices for an nxn grid). We can think of the
pathways as sequences of D's and R's, e.g. for a 3x3, DDDRRR is one pathway.
Now the problem is reduced to something similar to tracking coin  flips (let D
be heads and R be tails). Given that we must make 40 coin flips with exactly 20
of them heads, how many different sequences can result? 40choose20. Out of 40
decisions of going either down or to the right, choose 20 of them to be down.
"""

from scipy.special import comb


def PE15():
    return comb(40, 20, exact=True)


import timeit

start = timeit.default_timer()
answer = PE15()  # 137846528820 found in 1.6579037520614293e-05 seconds
elapsed = timeit.default_timer() - start
print("%s found in %s seconds" % (answer, elapsed))
