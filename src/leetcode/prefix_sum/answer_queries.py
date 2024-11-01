"""
Given an integer array nums, an array queries where queries[i] = [x, y] and an integer limit, return a boolean array that represents the answer to each query. A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.

For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13, the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].
"""
from typing import List


def answer_queries(nums: List[int], queries: List[List[int]], lim: int) -> List[bool]:
    n = len(nums)
    ps = nums[0] + [0] * (n - 1)
    for i in range(1, n):
        ps[i] += ps[i - 1]

    # sum[i:j] (inclusive) = ps[j] - ps[i - 1]
    ans = []
    for i, j in queries:
        if i == 0:
            _sum = ps[j]  # Return the partial sum directly.
        else:
            _sum = ps[j] - ps[i - 1]
        ans.append(bool(_sum < lim))
