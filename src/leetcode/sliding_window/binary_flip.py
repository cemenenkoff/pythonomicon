"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

0 <= k <= len(nums)

say k = 2

0  1  2  3  4  5  6  7

1  0  0  0  1  1  0  1
_______
   ____
      __________

"""
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lp = ans = curr = 0
        for rp in range(n):
            if nums[rp] == 0:
                curr += 1
            while curr > k:
                if nums[lp] == 0:
                    curr -= 1
                lp += 1
            ans = max(ans, rp - lp + 1)
        return ans
