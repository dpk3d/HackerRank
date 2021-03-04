"""
Given an array A of n positive numbers.
The task is to find the first Equilibium Point in the array.
Equilibrium Point in an array is a position such that the sum of elements before it is equal
to the sum of elements after it.
"""


# Time Complexity O( n * n ) Space Complexity O(n)
def findEquilibrium(arr):
    size = len(arr)
    if size == 1:
        return arr
    if size == 2:
        return - 1

    for x in range(size):
        left_sum = 0
        right_sum = 0

        for y in range(x):
            left_sum += arr[y]
        for y in range(x + 1, size):
            right_sum += arr[y]
        if left_sum == right_sum:
            return x
    return - 1


arr = [2, 3, 7, 8, 9, 1, 2]
print("Equilibrium Index is ==> ", findEquilibrium(arr))
"""
Result :
Equilibrium Index is ===>  3
"""



# Time Complexity O(n). Space O(n)
def getEquilibriumIndex(arr):
    left_sum = 0
    total_sum = sum(arr)
    size = len(arr)
    if size == 1:
        return arr
    if size == 2:
        return - 1

    for x, num in enumerate(arr):
        # Total Sum is Right sum for index x
        total_sum -= num
        if left_sum == total_sum:
            return x
        left_sum += num
    return -1


arr = [3, 4, 7, -2, 9, 5]
print("Equilibrium Index Optimized is ===> ", getEquilibriumIndex(arr))
"""
Result :
Equilibrium Index Optimized is ===>  3
"""
