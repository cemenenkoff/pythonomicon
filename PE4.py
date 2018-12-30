# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 10:09:45 2018

@author: Cemenenkoff
ProjectEuler.net Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
palindrome made from the product of two 3-digit numbers.
"""

def PE4(min=100,max=999):
    max_pal = 0
    for num1 in range(min,max+1):
        for num2 in range(num1,max+1): #*1
            prod = num1*num2
            if prod>max_pal and str(prod)==str(prod)[::-1]:#*2
                max_pal = prod
    return max_pal

"""
*1: Changing the lower bound to num1 avoids redundant calculations. For
example, when num1 starts at 100, 100*100 is checked first, followed by
100*101. After the rest of 100*102,100*103,...,100*999 are checked, num1
iterates to 101. When this occurs, there is no need to start with 101X100
because the instance has already been checked (because ab=ba). 101x101 is the
next relevant item.

*2: Notice also that FIRST we check if the product is larger than the maximum
palindrome found so far, because if it isn't, we should just move on without
taking the time to perform the more costly check to see if it's a palindrome.
"""
import timeit
start = timeit.default_timer()
answer = PE4() #906609 found in 0.03671574143040522 seconds
elapsed = (timeit.default_timer() - start)
print ('%s found in %s seconds' % (answer, elapsed))