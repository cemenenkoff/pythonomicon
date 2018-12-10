"""
Created on Wed Nov 21 12:58:37 2018
@author: Cemenenkoffsdf

Below, we answer projecteuler.org question #3.

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

import numpy as np

"""
My first thoughts were to obtain all primes below n, but then filter off the
ones that do not divide n. I started with an implementation of the Sieve of
Eratosthenes. The function below lists all positive prime numbers below an
integer n. My strategy was to get all primes below n, but then filter off the
ones which do not divide n. Once I understood that the filter is the heart of
answering the question, I realized that I could achieve the same result in a
much simpler manner. I left my initial work to act as a comparison between the
effeciency of these two functions in answering the question. It is better to
work smart rather than hard.
"""
def SOE(n):
    if type(n)!=int and n<0:
        return 'error: non-integer, non-positive input'
    elif type(n)!=int:
        return 'error: non-integer input'
    elif n<0:
        return 'error: non-positive input'
    elif n==0: #There are no positive primes below zero.
        return None
    #Construct a list of consecutive integers, 2 through n.
    thelist = []
    i = 2
    for i in range(n):
        thelist.append(i)
    #Starting from p, enumerate its multiples,counting to n in increments of p,
    #and remove said multiples from the list.
    plist=[2] #Initialize a list to store primes below n.
    tested=[] #Initialize a list to store tested multiples.
    for p in plist:
        i=2
        while p*i <= n:
            if p*i in tested:
                i+=1
            else:
                for number in thelist:
                    if number == p*i:
                        thelist.remove(number)
                        break
                tested.append(p*i)
                i+=1
        for number in thelist:
            if number>p:
                plist.append(number)
                break
    return thelist

"""
Unlike SOE(), PE3() answers the question directly. Note that we don't have to
check factors above sqrt(n) to determine if n is prime. The idea that started
this function was to keep dividing even n's by 2. Once all the twos are gone,
then we can divide out all the 3's, 5's, etc. Note that by dividing out ALL of
the 2's, we can ignore trying to divide out any more even numbers above 2.
"""
def PE3(n):
    for i in range(2,int(np.sqrt(n))):
        while n % i == 0:        #As long as i cleanly divides n,
            n //= i              #redefine n as the result of dividing n by i.
            if n == 1 or n == i: #If what remains is 1 or i, it means we've
                                 #"divided out" all factors of i, so
                return i         #return i as it is the largest factor. 

n=600851475143
print(PE3(n))
print(SOE(n))