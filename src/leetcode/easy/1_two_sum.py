"""
Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]


Constraints:
    2 <= nums.length <= 10**4
    -10**9 <= nums[i] <= 10**9
    -10**9 <= target <= 10**9
    Only one valid answer exists.


Follow-up: Can you come up with an algorithm that is less than O(n**2) time complexity?
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[num] = i


if __name__ == "__main__":
    """
    Why use a hashmap (i.e. dictionary) here? It allows us to check for the complement
    (`target - num`) in constant time O(1) on average. This is because dictionary
    lookups in Python are average O(1) (due to several technical factors).

    Additionally, the solution only requires a single pass through the array,
    completing the problem with O(n) time complexity rather than the naive O(n**2)
    approach involving nested loops. Since the hashmap stores up to `n` elements in the
    worst case, it has an O(n) space complexity.
    """
    print(Solution().two_sum(nums=[1, 2, 3], target=5))
