"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. Notice that the answer must
        be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        max_len = 0  # The max length of substrings without repeat chars.
        left = 0  # Marks the start of the current substring.
        char_set = set()  # Keeps track of characters in the current window.

        for right in range(len(s)):
            # If `s[right]` is already in the `char_set`, increment `left` until
            # `s[right]` is no longer a member, else add it (i.e. expand the window).
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            # Note that the `right - left + 1` ensures both endpoint positions are
            # counted in the sliding window.
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    """
    I first approached this problem but using a dynamically sliding window, but by
    calculating all possible windows first, then looping through them. Not only until I
    looked up the answer using pointers did I realize the power of dynamically-sliding
    windows. Not only does the window shrink and expand dynamically, the string is only
    passed over one time, giving it O(n) time complexity.
    """
    print(Solution().lengthOfLongestSubstring("aabcdeff"))
