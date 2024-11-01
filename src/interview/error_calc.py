"""
Amazon's database doesn't support very large numbers, and hence, numbers are stored as
a string of binary characters, '0' and '1'. Accidentally, a '!' was entered in some
positions, and it is unknown whether they should be '0' or '1'.

The string of incorrect data consists of the characters '0', '1', and '!', where '!'
represents an unknown character. The '!' can be replaced with either '0' or '1'. Due to
some internal faults, errors are generated every time the characters '0' and '1' appear
together as '01' or '10' in any subsequence of the string. It is observed that the
number of errors a subsequence '01' generates is x, while a subsequence '10' generates
y errors.

[Determine the minimum total errors generated]. Since the answer can be very large,
return it modulo 10^9 + 7.

Example:
    errorString = "101!1"
    x = 2
    y = 3

If the '!' at index 3 is replace with '0':
    The string is "10101". The number of times the subsequence 01 occurs is 3 at
    indices (1, 2), (1, 4), and (3, 4). The number of times the subsequence 10 occurs
    is also 3, indices (0, 1), (0, 3), and (2, 3). The number of errors is 3*x + 3*y =
    6 + 9 = 15.

If the '!' is replaced with '1':
    The string is "10111". The subsequence 01 occurs 3 times and 10 occurs 1 time. The
    number of errors is 3 * x + y = 9.

The minimum number of errors is min(9, 15) modulo (10^9 + 7) = 9.

Note: A subsequence of a string is obtained by omitting zero or more characters from
the original string without changing their order.

Hint: It can be proved that (a + b) % c = ((a % c) + (b % c)) % c, where a, b, and c
are integers and % represents the modulo operation.

Function Description
Complete the function getMinErrors.

getMinErrors has the following parameter(s):
    string errorString: a string of characters '0', '1', and '!'
    int x: the number of errors generated for every occurrence of subsequence 01
    int y: the number of errors generated for every occurrence of subsequence 10

Returns:
    int: the minimum number of errors possible, modulo 10^9 + 7.

Constrains:
    1 <= len(errorString) <= 10^5
    0 <= x, y <= 10^5
    s consists only of characters '0', '1', and '!'

Sample Case 0
STDIN | FUNCTION
0!!1!1 -> errorString = "0!!1!1"
2 -> x=2
3 -> y=3

Sample Output
10

Explanation:
All possibilites are as follows:
Serial Number | Possible String | Count of 01 | Count of 10 | Errors
1 | 000101 | 7 | 1 | 17
2 | 000111 | 9 | 0 | 18
3 | 001101 | 7 | 2 | 20
4 | 001111 | 8 | 0 | 16
5 | 010101 | 6 | 3 | 21
6 | 010111 | 7 | 1 | 17
7 | 011101 | 5 | 3 | 19
8 | 011111 | 5 | 0 | 10

The minimum number of errors is 10. Thus, the answer is 10.
"""

MOD = 10**9 + 7


def getMinErrors(errorString, x, y):
    # Count initial errors without replacing `!`
    n = len(errorString)

    # Precompute prefix counts of `0`s and `1`s for efficient calculation of errors
    prefix_zeros = [0] * n
    prefix_ones = [0] * n

    # Populate prefix counts
    for i in range(n):
        if i > 0:
            prefix_zeros[i] = prefix_zeros[i - 1]
            prefix_ones[i] = prefix_ones[i - 1]
        if errorString[i] == "0":
            prefix_zeros[i] += 1
        elif errorString[i] == "1":
            prefix_ones[i] += 1

    # Calculate minimum errors by considering each `!` as `0` or `1`
    total_errors_as_0 = 0
    total_errors_as_1 = 0
    min_errors = float("inf")

    # Number of `0`s and `1`s after each position
    total_zeros = prefix_zeros[-1]
    total_ones = prefix_ones[-1]

    # Iterate and calculate errors dynamically
    count_zeros = 0  # Count of '0's encountered so far
    count_ones = 0  # Count of '1's encountered so far

    for i in range(n):
        if errorString[i] == "0":
            # Adds to `10` errors for each preceding `1`
            total_errors_as_1 += count_ones * y
            total_errors_as_1 %= MOD
            count_zeros += 1
        elif errorString[i] == "1":
            # Adds to `01` errors for each preceding `0`
            total_errors_as_0 += count_zeros * x
            total_errors_as_0 %= MOD
            count_ones += 1
        elif errorString[i] == "!":
            # Option 1: Replace `!` with '0'
            option_as_0 = (total_errors_as_0 + (count_ones * y) % MOD) % MOD

            # Option 2: Replace `!` with '1'
            option_as_1 = (total_errors_as_1 + (count_zeros * x) % MOD) % MOD

            # Choose the minimum error count
            min_errors = min(min_errors, option_as_0, option_as_1)

            # Update running totals as if we replaced with '0' or '1'
            total_errors_as_0 = option_as_0
            total_errors_as_1 = option_as_1
            count_zeros += 1  # Assume replacing with '0' for the next step

    return min_errors % MOD


# Test case
print(getMinErrors("101!1", x=2, y=3))  # Expected output: 9
