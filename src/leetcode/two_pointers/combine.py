"""
Given two sorted integer arrays `arr1` and `arr2`, return a new array that combines both of them and is also sorted.

`arr1` = [1, 2, 5, 7, 8, 9]
`arr2` = [4, 6, 9]

"""


def combine(arr1, arr2):
    p1 = 0
    p2 = 0
    n = len(arr1)
    m = len(arr2)
    res = []
    while p1 < n and p2 < m:
        if arr1[p1] <= arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        else:
            res.append(arr2[p2])
            p2 += 1
    if p1 < n:
        res.extend(arr1[p1:])
    if p2 < m:
        res.extend(arr2[p2:])
    return res


arr1 = [1, 2, 5, 7, 8, 9]
arr2 = [4, 6, 9]
print(combine(arr1, arr2))
