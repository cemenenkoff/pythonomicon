# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:58:22 2018

@author: Cemenenkoff

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?

Consider m=sqrt(n), meaning m*m=n. If n is composite, then n=a*b. Now there are
three cases:
    (1) If a=m=b, then we must check up to sqrt(n) to confirm n is composite.
    (2) If a>sqrt(n), then b<sqrt(n), so checking up to sqrt(n) ensures we will
        encounter b, which then confirms n is composite.
    (3) If a<sqrt(n), then b>sqrt(n), so checking up to sqrt(n) ensures we will
        encounter a, which then confirms n is composite.
To show n is prime, it is enough to show that n is not composite. Thus, if we
check factors up to ceil(sqrt(n)) (to be safe) and still cannot find one that
divides n, we may conclude n is not composite and is therefore prime.
"""

import numpy as np
def is_prime(n):
    if n%2==0: #Return False if the number is even.
        return False
    else: #Instead, if the number is odd:
        for possible_factor in range(3, int(np.ceil(np.sqrt(n)))+1, 2):#*1
            if n%possible_factor==0:
                return False
        return True
        
#1*: Notice we skip by 2 to only check odd numbers. The +1 is added for the
#case of 9 to avoid range(3,3).
#print(is_prime(104729))
#print(is_prime(9))

def PE7(n):
    count = 1
    for num in range(3, n*n, 2):#*2
        if is_prime(num)==True:
            count+=1
            if count==n:
                return num
    if count<n:
        return 'lift ceiling'

#2*: Again we skip by 2 to only check odd numbers. The ceiling is arbitrary,
#and should be lifted if the desired count isn't reached.

import time
start = time.time()
answer = PE7(10001)
elapsed = (time.time() - start)
print ('%s found in %s seconds' % (answer, elapsed))
#104743 found in 0.182511568069458 seconds