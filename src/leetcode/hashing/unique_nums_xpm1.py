"""
Given an integer array nums, find all the unique numbers x in nums that satisfy the following: x + 1 is not in nums, and x - 1 is not in nums.
"""

def find_unique_nums(nums):
    ans = []
    nums = set(nums)  # Remember that a set is a hash map where the keys don't map to anything.
    for x in nums:
        if x + 1 not in nums and x - 1 not in nums:
            ans.append(x)
