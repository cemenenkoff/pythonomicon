"""
1732. Find the Highest Altitude
Solved
Easy
Topics
Companies
Hint
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.



Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.


Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100

SOLVED IN: 28:09
"""
from typing import List

class Solution:
    """
    n = 10 -> num_points = 11

        o                             x  <-- n
        0  1  2  3  4  5  6  7  8  9 10
           i
        0  1  2  3  2  5  0  0  0  1  0

    5                  _
    4
    3            _
    2         _     _
    1      _                       _
    0   _                 _  _  _

    """
    def largestAltitude(self, gain: List[int]) -> int:
        # prefix sum to track net gain
        n = len(gain)
        ans = curr = 0
        for i in range(n):
            curr += gain[i]
            ans = max(ans, curr)
        return ans
