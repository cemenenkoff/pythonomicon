"""
You are given a string s and an integer k. Find the length of the longest substring that contains at most k distinct characters.
"""

from collections import defaultdict

def find_longest_substring(s: str, k:int) -> int:
    counts = defaultdict(int)
    lp = ans = 0
    n = len(s)
    for rp in range(n):             # rp embedded in range(n)
        counts[s[rp]] += 1          # Increment curr
        while len(counts) > k:      # If window is invalid
            counts[s[lp]] -= 1      # Decrement curr + optional other logic
            if counts[s[lp]] == 0:
                del counts[s[lp]]
                lp += 1             # lp += 1
        ans = max(ans, rp - lp + 1)
    return ans