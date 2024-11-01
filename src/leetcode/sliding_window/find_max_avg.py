"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # sliding window, fixed
        n = len(nums)
        ans = curr = sum(nums[:k]) / k
        for i in range(k, n):
            curr += (nums[i] - nums[i - k]) / k
            ans = max(ans, curr)
        return ans
