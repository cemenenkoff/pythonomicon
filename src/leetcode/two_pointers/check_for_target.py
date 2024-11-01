"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""


def check_for_target(arr, k) -> bool:
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        _sum = arr[left] + arr[right]
        if _sum == k:
            return True
        # If we have `left + right > target`, then we can never have a solution with
        # `right`, because `left` can only increase (and vice versa).
        if _sum > k:
            right -= 1
        else:
            left += 1
    return False
