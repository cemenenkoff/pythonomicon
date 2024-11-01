"""
Given an array `nums`. We define a running sum of an array as:
    runningSum[i] = sum(nums[0] … nums[i])

Return the running sum of nums.
"""
from typing import List


def get_running_sum(nums: List[int]) -> List[int]:
    """
          i        x
    0  1  2  3  4  5
    2  1  0  0  1

    """
    n = len(nums)
    for i in range(1, n):
        nums[i] += nums[i - 1]
    return nums
