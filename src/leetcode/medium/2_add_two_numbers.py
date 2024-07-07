"""
You are given two non-empty linked lists representing two non-negative integers. The
digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0
itself.

Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.

Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

from typing import Optional


class ListNode:
    """Note that a linked list is visualized like [Head] -> [Node] -> ... -> [Tail]"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode()  # The dummy head of this linked list is 0.
        tail = dummy_head
        carry = 0

        while l1 or l2 or carry:
            # Grab the digits according to their place value.
            dig1 = l1.val if l1 else 0
            dig2 = l2.val if l2 else 0

            # Sum them to find the next digit (and calculate any carry-over).
            sum_ = dig1 + dig2 + carry
            carry = sum_ // 10
            dig = sum_ % 10

            tail.next = ListNode(val=dig)  # Extend the linked list with another node.

            tail = tail.next  # Update the tail to be the newly-added node.
            l1 = l1.next if l1 else None  # Update the next digit in `l1`.
            l2 = l2.next if l2 else None  # Do the same for `l2`.

        return dummy_head.next


if __name__ == "__main__":
    """
    My approach to this problem was to try to understand why linked lists are so
    powerful. Despite looking a bit clunky, unlike arrays, linked can dynamically grow
    or shrink as needed, have efficient insertions or deletions, and don't waste any
    space.

    While linked lists are not as commonly used in Python as built-in data structures
    like `list` or colloections like `deque` (double-ended queue), they are still
    relevant in an educational context.
    """
    # Example 1
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    result = Solution().add_two_numbers(l1, l2)
    # Print the result in the expected output format.
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(f"Example 1: {output}")

    # Example 2
    l1 = ListNode(0)
    l2 = ListNode(0)
    result = Solution().add_two_numbers(l1, l2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(f"Example 2: {output}")

    # Example 3
    l1 = ListNode(
        9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    )
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    result = Solution().add_two_numbers(l1, l2)
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(f"Example 3: {output}")
