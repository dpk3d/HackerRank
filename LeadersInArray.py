"""
Given an array A of positive integers. Your task is to find the leaders in the array.
An element of array is leader if it is greater than or equal to all the elements to its right side.
The rightmost element is always a leader.
"""


# Time Complexity O (n * n) , Brute Force Approach
def findLeaderSimple(arr):
    size = len(arr)
    for x in range(0, size):
        for y in range(x + 1, size):
            if arr[x] < arr[y]:
                break
        if y == size - 1:
            print("Leaders in Given Array is ===>", arr[x])


deepak = [1, 4, 3, 2, 5, 17, 4, 3, 8, 1]
findLeaderSimple(deepak)
"""
Output :
Leaders in Given Array is ===> 17
Leaders in Given Array is ===> 8
Leaders in Given Array is ===> 1
"""


# Optimal Approach , Time Complexity O(n)
def findLeaderOptimal(arr):
    size = len(arr)
    max_element_Right = arr[-1]
    print("Leader in Array ==>", max_element_Right)
    for x in range(size - 2, -1, -1):
        if max_element_Right < arr[x]:
            print("Leaders in Array ==>", arr[x])
            max_element_Right = arr[x]


deepak = [1, 4, 3, 2, 5, 17, 4, 3, 8, 1]
print("Leaders in Given Array is ===>", findLeaderOptimal(deepak))
"""
Output :
Leader in Array ==> 1
Leaders in Array ==> 8
Leaders in Array ==> 17
"""
