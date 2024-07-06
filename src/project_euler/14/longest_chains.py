# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 13:44:06 2019

@author: Cemenenkoff

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
import numpy as np


def evens_within(start, end):
    if start % 2 == 0:
        startmap = start / 2
    else:
        startmap = (start + 1) / 2
    if end % 2 == 0:
        endmap = (end - 2) / 2
    else:
        endmap = (end - 1) / 2
    diff = end - start
    if diff % 2 == 0:
        num_evens = diff / 2  # number of even ints in [start_, end_)
    else:
        if start % 2 == 0:
            num_evens = np.ceil(diff / 2)
        else:
            num_evens = diff // 2
    print(
        "The %6d even integers from [%6d, %-7d) map out [%6d, %-6d]"
        % (num_evens, start, end, startmap, endmap)
    )
    return startmap, endmap + 1


"""
At first I thought to only use brute force, but that seemed like a cop out.
After thinking for a while, I've finally proven we can do a little bit better
than brute force by changing the range call from (1, 10**6) to (500000, 10**6).

Instead of checking all Collatz sequences from 1 to 10**6, we only need to
check from 500000 to 10**6. The reason being can be seen from the results of
the while loop involving evens_within():

start = 500000
end = 1000000
while end>start+1:
    start, end = evens_within(start,end)
>>>>
The 250000 even integers from [500000, 1000000) map out [250000, 499999]
The 125000 even integers from [250000, 500000 ) map out [125000, 249999]
The  62500 even integers from [125000, 250000 ) map out [ 62500, 124999]
The  31250 even integers from [ 62500, 125000 ) map out [ 31250, 62499 ]
The  15625 even integers from [ 31250, 62500  ) map out [ 15625, 31249 ]
The   7812 even integers from [ 15625, 31250  ) map out [  7813, 15624 ]
The   3906 even integers from [  7813, 15625  ) map out [  3907, 7812  ]
The   1953 even integers from [  3907, 7813   ) map out [  1954, 3906  ]
The    977 even integers from [  1954, 3907   ) map out [   977, 1953  ]
The    488 even integers from [   977, 1954   ) map out [   489, 976   ]
The    244 even integers from [   489, 977    ) map out [   245, 488   ]
The    122 even integers from [   245, 489    ) map out [   123, 244   ]
The     61 even integers from [   123, 245    ) map out [    62, 122   ]
The     31 even integers from [    62, 123    ) map out [    31, 61    ]
The     15 even integers from [    31, 62     ) map out [    16, 30    ]
The      8 even integers from [    16, 31     ) map out [     8, 15    ]
The      4 even integers from [     8, 16     ) map out [     4, 7     ]
The      2 even integers from [     4, 8      ) map out [     2, 3     ]
The      1 even integers from [     2, 4      ) map out [     1, 1     ]

By definition, if we begin a Collatz sequence with an even integer n, we are
going to produce the next n via n = n/2. Notice that n/2's Collatz sequence is
nested within n's. This means that by checking for the length of n's Collatz
sequence, we already know that the length of n/2's Collatz sequence will be one
less than the length of n's. Since we are only concerned with finding the
Collatz sequence of maximal length, we needn't check numbers we know beforehand
have a sequence length less than the current maximum.

Notice if we connect all of the mapped out intervals, they produce [1,499999]
(square brackets to indicate inclusivity), precisely the numbers we skipped
checking by starting at 500000 instead of 1.
"""


def PE14():
    max_chain = 0
    max_n = 0
    for n in range(500000, 10**6):
        n_ = n  # save the original n for later
        chain = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            chain += 1
        if chain > max_chain:
            max_chain = chain
            max_n = n_
    return max_n


import timeit

start = timeit.default_timer()
answer = PE14()  # 837799 found in 8.745221884817056 seconds
elapsed = timeit.default_timer() - start
print("%s found in %s seconds" % (answer, elapsed))
