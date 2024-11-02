"""
560. Subarray Sum Equals K
Solved
Medium
Topics
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""
from typing import List

from collections import defaultdict, Counter

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        # hm = Counter({0: 1})  # tracking ps counts, 0 is counted once for the starting ind.
        n = len(nums)
        ps = ans = 0
        for i in range(n):
            ps += nums[i]
            sum_complement = ps - k
            ans += hm[sum_complement]
            hm[ps] += 1
        return ans
