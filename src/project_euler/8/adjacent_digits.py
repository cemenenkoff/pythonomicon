# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 12:39:51 2018

@author: Cemenenkoff

The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""


def PE8_for():
    with open("PE8.txt") as f:
        lines = f.readlines()
    # Remove characters like '\n' at the end of each line with .strip()
    lines = [x.strip() for x in lines]
    # Concatenate everything into one string and then convert it to an integer.
    number_str = "".join(lines)

    # Now we are going to slide across this number from left to right with a
    # slider that is 13 digits long. For example, if we had a 3-digit-long
    # slider on the number 9876789, our analysis would look like:
    #    [987]6789, 9[876]789, 98[767]89, 987[678]9, 9876[789]

    number_len = len(number_str)  # Find the amount of digits in the number.
    slider_len = 13  # We have slider with space for 13 consecutive digits.
    max_product = 0
    # Stop once the slider reaches the last possible 13-digit string.
    for i in range(0, number_len - slider_len + 1):
        # list() makes each 13-digit-long string a list of 1-char-long strings.
        digits = list(number_str[i : i + 13])
        if "0" in digits:  # If '0' is found, slide to the right by 1. See *1.
            continue
        product = 1
        for digit in digits:
            product = product * int(digit)
            if product > max_product:
                max_product = product
    return max_product


import timeit  # Better than the time module to find speeds of solutions.

start = timeit.default_timer()
answer = PE8_for()  # 23514624000 found in 0.0009942546320473866 seconds
elapsed_for = timeit.default_timer() - start
print("%s found in %s seconds" % (answer, elapsed_for))

"""
*1: I'm satisfied with my answer, but I see a way it could be optimized. If a
chunk of 13-digits in the slider contains a '0', we can log the rightmost 0's
index and then move the slider such that the '0' it found is immediately on the
left (outside of the slider) before checking for '0' again. This means we move
the slider to the right by k positions if '0' is found at position 0<=k<=12 in
the slider. For example:
    i=0, so we start with [900]6754. The rightmost 0 is at index 2.
    Next, shift i by 2 such that the slider's position represents 90[067]54.
    i iterates with a continue statement, thus i=3 now.
    The process begins again with 900[675]4.
    Repeat these steps until 9006[754] is tested.
After some digging though, this type of index shift is more well-suited to use
with while loops. If given something like
    for i in range(10):
        if i==2:
            i+=5
        print(i)
there will still be ten print statements (0,1,7,3,...,8,9), so the best we can
do with a for loop is use a continue statement to bump the slider index over by
1 if a '0' is encountered.
"""


def PE8_while():
    with open("PE8.txt") as f:
        lines = f.readlines()
    # Remove characters like '\n' at the end of each line with .strip()
    lines = [x.strip() for x in lines]
    # Concatenate everything into one string.
    number_str = "".join(lines)

    # Now we are going to slide across this number from left to right with a
    # slider that is 13 digits long. For example, if we had a 3-digit-long
    # slider on the number 9876789, our analysis would look like:
    #    [987]6789, 9[876]789, 98[767]89, 987[678]9, 9876[789]

    number_len = len(number_str)  # Find the amount of digits in the number.
    slider_len = 13  # We have slider with space for 13 consecutive digits.
    max_product = 0
    i = 0  # i represents the index of the leftmost position in the slider relative
    # to the entire number_str.
    # Stop once the slider reaches the last possible 13-char-long string.
    while i <= number_len - slider_len:
        # list() turns the 13-char-long string of number_str under consideration
        # into a list of 1-char-long strings.
        digits = list(number_str[i : i + slider_len])
        digits = digits[::-1]  # Reverse the digits so we can find the rightmost
        if "0" in digits:  # zero in the unreversed list first with index.
            skip = slider_len - digits.index("0")
            i += skip
            continue
        product = 1
        for digit in digits:
            product *= int(digit)
        if product > max_product:
            max_product = product
        i += 1
    return max_product


start = timeit.default_timer()
answer = PE8_while()  # 23514624000 found in 0.000848456625703875 seconds
elapsed_while = timeit.default_timer() - start
print("%s found in %s seconds" % (answer, elapsed_while))

print("for/while = %s" % (elapsed_for / elapsed_while))
"""
After implementing the while loop, we see that it is actually about 15% faster
in this situation.
"""
