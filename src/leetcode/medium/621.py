import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        AAAA BB CC, n=2
        When it comes to deciding the order, A is the limiting factor because if BC pairs are done first, consecutive As will incur idle time. So we must fill in the backbone structure of separated As.
            A _ _ A _ _ A _ _ A
            A B C A B C A _ _ A
        Notice this is 3 blocks and a bookend:
            3*`A _ _` + `A`
        We could write the number of slots as:
            `slots` = (`max_count` - 1) * (n + 1) + 1
        But the bookend isn't always 1. Right now it is just A. What if instead we have multiple tasks with the `max_count`? Then the bookend is just that number of tasks.
        AAAA BBBB CC, n=2
            A B _ A B _ A B _ A B
            3*`AB_` + `AB`
            (`max_count` - 1) * (n + 1) + `num_max_count_tasks`

        Now we consider having such a large variety of tasks that no cooling slots are necessary to calculate:
            AAAABBBCCCDEFGHIJK...XYZ, n=2
            A _ _ A _ _ A _ _ A
            A B C A B C A B C A D E F G H ... X Y Z
            len(tasks) (i.e. the minimum number of slots possible)

        So the number of slots is `max(slots, len(tasks))`
        """

        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        max_count_tasks = sum(1 for freq in task_counts.values() if freq == max_count)
        slots = (max_count - 1) * (n + 1) + max_count_tasks
        slots = max(slots, len(tasks))
        return slots


tasks = ["A"] * 3 + ["B"] * 3
soln = Solution()
soln.leastInterval(tasks=tasks, n=2)
