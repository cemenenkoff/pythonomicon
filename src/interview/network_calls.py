"""
The marketing team at Amazon is experimenting with the number of reviews for each producet.

You are given an array `reviews` of size n, where `reviews[i]` represents the number of reviews for the ith product. There are APIs available to add or remove reviews, where each API call can either add or remove one review.

Given an integer array `counts` of size q, your task is to calculate the number of API calls required to change the review count of each product to match each value in the array `counts`.

The goal is to return an array of size q, where the ith element denotes the total number of API calls needed to change the review count of all products to match counts[i].

Example
n=5
reviews = [4,6,5,2,1]
q=1
counts=[3]

Value | Additions/Removals Needed | API Calls
4 | 1 removal | 1
6 | 3 removals | 3
5 | 2 removals | 2
2 | 1 addition | 1
1 | 2 additions | 2

Therefore, the total API calls made to change the number of reviews for all products to 3 is: (1 + 3 + 2 + 1 + 2) = 9.
Hence, return the array [9].

Function Description
Complete the function findNetworkCalls in the editor below.
findNetworkCalls has the following parameters:
int reviews[n]: the initial count of reviews of each product
int counts[q]: the equal count of reviews

Returns
long[q]: the number of API calls to be made to change the review count of each product.

Constraints:
1 <= n <= 2*10^5
1 <= reviews[i] <= 10^9
1 <= q <= 2 * 10^5
1 <= counts[i] <= 10^9

Input Format for Custom Testing
The first line contains an integer n, the number of the products.
Each line i of the n subsequent lines contains an integer denoting reviews[i].
The next line contains an integer q, the number of different values to be experimented with.
Each line i of the q subsequent lines contains an integer describing counts[i]

Sample Input for Custom Testing
For counts value 6:
Value x | Additons/Removals Needed | API Calls
3 | 3 additions | 3
6 | no addition/removal needed | 0
2 | 4 additions | 4
6 | no addition/removal needed | 0
3 | 3 additions | 3
So, the total number of API calls to change the review counts to 6 is: 3 + 0 + 4 + 0 + 3 = 10

Similarly for counts value 8:
The total number of API calls to change the review counts to 8 is: 5 + 2 + 6 + 2 + 5 = 20.
Hence, return the array [10, 20].


Another sample case....
Sample Output:
4
3

Explanation:
For counts value 5:
The total number of API calls to be made is: 2 + 1 + 1 = 4
For counts value 6:
The total number of API calls to be made is: 3 + 0 + 0 + 3.
Hence, return an array [4,3].
"""

from typing import List


def findNetworkCalls(reviews: list, counts: List[int]) -> int:
    n = len(reviews)
    result = []
    for count in counts:
        api_calls = 0
        for review in reviews:
            api_calls += abs(review - count)
    result.append(api_calls)
    return result


"""
To optimize, we must address the inefficiency of iterating over `reviews` repeatedly.
We will use pre-sorting and prefix sums.

1. Sort `reviews`
2. Use prefix sums to compute the total API calls for each `counts[i]`:
    - Precompute the sum of reviews once.
    - For each `counts[i]`, use binary search to find the position in the sorted `reviews` where the review count should be inserted. This allows us to split the array into two parts:
        - Reviews less than or equal to `counts[i]`: We calculate the API calls required to increase these reviews.
        - Reviews greater than `counts[i]`: we calculate the APU calls required to decrease these reviews.
"""
import bisect


def findNetworkCalls(reviews, counts):
    # Step 1: Sort the reviews and precompute prefix sums
    reviews.sort()
    n = len(reviews)

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + reviews[i - 1]

    result = []

    # Step 2: Process each count using binary search and prefix sums
    for count in counts:
        # Find the position where count would fit in the sorted reviews array
        pos = bisect.bisect_left(reviews, count)

        # Sum of reviews less than or equal to count
        left_sum = prefix_sum[pos]
        # Sum of reviews greater than count
        right_sum = prefix_sum[n] - left_sum

        # API calls to increase the left side reviews to count
        increase_calls = count * pos - left_sum
        # API calls to decrease the right side reviews to count
        decrease_calls = right_sum - count * (n - pos)

        total_calls = increase_calls + decrease_calls
        result.append(total_calls)

    return result
