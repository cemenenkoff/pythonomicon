"""
283. Move Zeroes
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        0  1  2  3  4  5  6  7
              |
        1  2  0  0  0  1  1  4
                       |
        """
        n = len(nums)
        lp = winlen = 0
        for rp in range(n):
            if nums[rp] == 0:
                winlen += 1
            else:
                nums[rp], nums[rp - winlen] = (nums[rp - winlen], nums[rp])
                lp += winlen
