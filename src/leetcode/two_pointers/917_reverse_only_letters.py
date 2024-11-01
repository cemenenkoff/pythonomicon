"""
917. Reverse Only Letters
Solved
Easy
Topics
Companies
Hint
Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.



Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Constraints:

1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.
"""


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        lowers = "abcdefghijklmnopqrstuvwxyz"
        uppers = lowers.upper()
        letters = list(lowers + uppers)
        lp = 0
        n = len(s)
        chars = list(s)
        rp = n - 1
        while lp < rp:
            if chars[lp] in letters and chars[rp] in letters:
                chars[lp], chars[rp] = (chars[rp], chars[lp])
                lp += 1
                rp -= 1
            if chars[lp] not in letters:
                lp += 1
            if chars[rp] not in letters:
                rp -= 1
        return "".join(chars)
