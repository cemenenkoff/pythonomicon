"""
268. Missing Number
Easy
Topics
Companies
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.


Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        0  1  2  3  4  5  <-- n = 6, so the range is [0, 6] (inclusive, so 7 nums)
        5  4  6  3  7  1
        """
        # How I would most likely think of it, since hashmaps are good for tracking
        # things we've previously encountered.
        n = len(nums)
        hm = set(nums)
        for i in range(n + 1):
            if i not in hm:
                return i

        # For the clever way:
        n = len(nums)
        tot = n * (n + 1) // 2
        return tot - sum(nums)