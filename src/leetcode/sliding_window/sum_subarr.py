"""
Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.
"""


def find_max_subarr_sum(nums, k) -> int:
    n = len(nums)
    ans = curr = sum(nums[:k])
    for i in range(k, n):
        curr += nums[i] - nums[i - k]
        ans = max(ans, curr)
    return ans
