"""
Given an array of positive integers `nums` and an integer `k`, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.
"""


def find_length(nums, k) -> int:
    left = 0
    _sum = 0
    max_len = 0
    for right in nums:
        _sum += nums[right]
        while _sum > k:  # while window is invalid
            _sum -= nums[left]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len
