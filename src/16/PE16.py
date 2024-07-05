# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 11:05:20 2019

@author: Cemenenkoff

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

This problem was awesome because it built off of work I did for problem 13
which involved summing one-hundred 50-digit numbers. The strategy is to take a
number, say 8192, and convert it to a string -> '8192'. Then we stack the
number along with a copy of itself into a numpy array and sum by column to
return a list of strings:
    8  1  9  2
    8  1  9  2
  + __________
   16  2 18  4
>>>>['16', '2', '18', '4']

Then we leftpad each entry in the list with 0s so they are all the same length
(with the leftpad_zeros() function):
>>>>['16, '02', '18', '04']

And then "restack" and "resum" them (with the restack_resum() function):
    [1 6 0 0 0]
    [0 0 2 0 0]
    [0 0 1 8 0]
    [0 0 0 0 4]
  + ___________
>>>>['1','6','3,'8',4']
>>>>'16384'

If we start with '1' and run this process 1000 times, we'll end up with all of
the digits that represent 2**1000 in a string. Then with a quick
    tot=0
    for digit in digits:
        tot+=int(digit),

we end up with our desired digit sum.

"""

import numpy as np
#This function takes a list of strings, finds the length of the strings(s) with
#the most characters, and then leftpads 0s on all of the strings with less
#characters so all of the strings in the list become the same length.
def leftpad_zeros(numlist):
    widest_len = len(max(numlist, key=len))
    for i, numstring in enumerate(numlist):
        width_diff = widest_len - len(numstring)
        if width_diff>0:
            numlist[i] = width_diff*'0'+numstring
    return numlist

#This function takes a list of strings, each of which represents a number with
#a certain amount of digits, and then "staggers" them all in a matrix, e.g.
#an input of sumcols = ['31', '32', '33', '34'] would create
    #[3 1 0 0 0]
    #[0 3 2 0 0]  <-- This is the sumgrid numpy array.
    #[0 0 3 3 0]
    #[0 0 0 3 4]
#It then sums all numbers in the matrix column-by-column and returns the sums
#as a list of strings. The above example outputs
#    sumcols_new = ['3', '4', '5', '6', '4'].
def restack_resum(sumcols):
    #Stacking is easy when all of the strings have the same length, so ensure
    #this by running leftpad_zeros if the strings aren't all the same length.
    if all(len(num)==len(sumcols[0]) for num in sumcols) == False:
        sumcols = leftpad_zeros(sumcols)
    #Once the numbers are all the same length, we will acquire precisely
    #len(sumcols)+len(sumcols[0])-1 additional columns.
    sumgrid = np.zeros((len(sumcols),len(sumcols)+len(sumcols[0])-1))
    for i, number in enumerate(sumcols):
        for j, digit in enumerate(number):
            sumgrid[i,i+j] = digit
    #Once the numbers are stacked up nicely, sum them up column-by-column.
    sumcols_new = np.sum(sumgrid, axis=0)
    #Convert the row of integers into strings with list comprehension.
    sumcols_new = ["%d" % number for number in sumcols_new]
    return sumcols_new

def dbl_digs(digs):
    #Initialize a 2xlen(digs) matrix of zeros. Each column represents
    #descending place value holders for digits.
    numgrid = np.zeros((2,len(digs)))
    for j, digit in enumerate(digs):
        numgrid[0,j] = digit
    numgrid[1]=numgrid[0]
    
    #Sum the entries of each column and then convert the sums to strings for
    #use in leftpad_zeros() and restack_resum().
    sumcols = np.sum(numgrid, axis=0) #Sum the digits columnwise from the left.
    #Convert the digits into a list of strings.
    sumcols = ["%d" % number for number in sumcols]
    #Restack the column sums incase there was rollover (e.g. 8+8=16, so the
    #two-digit sum causes a restack).
    digs = restack_resum(sumcols)
    digs = ''.join(digs) #Concatenate the list of strings.
    digs = digs.lstrip('0') #Strip any leading 0's.
    return digs #Return the new digits.

def PE16():
    digs='1'
    for i in range(1000):
        digs=dbl_digs(digs)
    tot=0
    print(digs)
    for dig in digs:
        tot+=int(dig)
    return tot

import timeit
start = timeit.default_timer()
answer = PE16() #1366 found in 0.2048620465602653 seconds
elapsed = (timeit.default_timer() - start)
print('%s found in %s seconds'%(answer, elapsed))