"""
You are given a binary string `s` (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.
"""


def find_len_bin(s) -> int:  # [110]11011
    n = len(s)
    left = 0
    curr = 0
    max_len = 0
    for right in range(n):
        if s[right] == "0":  # Only allow one zero.
            curr += 1
        while curr > 1:  # window is invalid:
            if s[left] == "0":
                curr -= 1
            left += 1
        max_len = max(max_len, right - left + 1)
