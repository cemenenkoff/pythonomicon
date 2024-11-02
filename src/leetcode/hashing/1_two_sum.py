"""
Given an array of integers nums and an integer target, return indices of two numbers such that they add up to target. You cannot use the same index twice.

"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in ht:  # Have we already found the complement?
                return [ht[complement], i]
            ht[num] = i