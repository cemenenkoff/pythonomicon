"""
1941. Check if All Characters Have Equal Number of Occurrences
Solved
Easy
Topics
Companies
Hint
Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.

"""

from collections import defaultdict, Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # As a 1-liner:
        return len(set(Counter(s).values())) == 1

        # To better illustrate using the concept of a hashmap:
        hm = defaultdict(int)
        for ch in s:
            hm[ch] += 1
        return all(freq == hm[s[0]] for freq in hm.values())