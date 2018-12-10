# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:01:17 2018

@author: Cemenenkoff

2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?
"""
#Note that the number is at minimum a product of the primes below 20.
#9699690=2*3*5*7*11*13*17*19
def PE5():
    for num in range(9699690,10**9,10): #Skipping by 10s, we get 2 and 5 free.
        if ((((num/2)/2)/2)%2)==0: #Next we check 16 and get 4, 8, and 20 free.
            if ((num/3)%3)==0: #Next is 9 which gives us 6, 12, 15, 18 free.
                if num%7==0: #Check 7 and get 14 free.
                    if num%11==0: #Check 11.
                        if num%13==0: #Check 13.
                            if num%17==0: #Check 17.
                                if num%19==0: #Check 19.
                                    return num

import time
start = time.time()
answer = PE5()
elapsed = (time.time() - start)
#232792560 found in 5.440448999404907 seconds

print ('%s found in %s seconds' % (answer,elapsed))

"""
The answer can actually be found directly by starting with 2*3*5*7*11*13*17*19 
and then incrementing the powers by looking at the prime factorizations of each
divisor starting from 20 downward; choosing increment when a factor requires a
greater power on a subfactor. For example, 20=2**2*5 requires 2**2, so
change the starting number to (2**2)*3*5*7*11*13*17*19. Next, 18=3**2*2
requires 3**2, so the starting number changes to (2**2)*(3**2)*5*7*11*13*17*19.
Next, 16=2**4 requires 2**4, so we have (2**4)*(3**2)*5*7*11*13*17*19. Note
that all the other divisors' prime factorizations can be constructed from these
factors, so the answer is (2**4)*(3**2)*5*7*11*13*17*19 = 232792560.

To automate this process, we'd first start with a product of the primes below
the largest of the divisors we need to check. Then, we'd need a function to
efficiently return the prime factorization of a number. We'd then use this
function on the largest divisor first, seeing if there are any powers to
increment, and then move downward. Once 2 is reached, the process stops.
Depending on the maximum divisor, the code could be optimized to avoid checking
certain redundancies (e.g. if 32 is checked, skip the smaller powers of 2).
"""