"""
Given an array of distinct integers.
The task is to count all the triplets such that sum of two elements equals the third element.
"""

array = [2, 3, 4, 5, 7, 8, 9, 10]
unsortedArray = [2, 8, 7, 9, 4, 3, 5, 10]


def triplets(arr, s):
    result = []
    for i in range(len(arr)):
        result.append(arr[i])
        checkZero = s - sum(result)

        while checkZero == 0:
            return result


print(triplets(array, 21))


def tripletsWithUnsortedArray(arr, s):
    result = []
    for i in range(len(arr)):
        result.append(arr[i])
        while sum(result) > s:
            result.pop(0)
        if sum(result) == s:
            return result


print(tripletsWithUnsortedArray(unsortedArray, 20))
