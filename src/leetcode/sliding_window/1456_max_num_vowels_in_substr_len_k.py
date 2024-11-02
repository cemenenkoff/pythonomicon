"""
1456. Maximum Number of Vowels in a Substring of Given Length
Solved
Medium
Topics
Companies
Hint
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.



Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length

"""
class Solution:
    """  k = 3

    |     |
    0  1  2  3  4  5  6  7  8  9
    a  b  c  i  a  i  d  e  f  x
                |     |


    """
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = "aeiou"
        curr = sum(1 for ch in s[:k] if ch in vowels)
        ans = curr
        for i in range(k, n):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1
            ans = max(ans, curr)
        return ans
