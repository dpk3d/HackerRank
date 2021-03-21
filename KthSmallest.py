"""
Given an array arr[] and a number K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.
"""


# Using Sorting Algorithm like Merge Sort and Heap Sort .
# Time Complexity is O (n long n)
def KthSmallestEasyMethod(arr, k):
    arr.sort()
    return arr[k - 1]
    # return arr[ -k] , Gives the Kth Largest Element


array = [2, 13, 8, 9, 5, 7, 4, 19]
k = 3
print("Kth Smallest Element", KthSmallestEasyMethod(array, k))
# Kth Smallest Element 5

import sys


def KthSmallestOptimal(array, left, right, k):
    # k is smaller then number of element in Array
    if 0 < k <= right - left + 1:
        # QuickSort
        position = partition(array, left, right)
        # If position is same as k
        if position - left == k - 1:
            return array[position]
        if position - left > k - 1:
            # Position is in Left
            return KthSmallestOptimal(array, left, position - 1, k)
        # Position is in Right Array
        return KthSmallestOptimal(array, position + 1, right, k - position + left - 1)

    # If k is more than elements in Array
    return sys.maxsize


# QuickSort, takes last element as pivot and moves all smaller element to left side
# and greater elements to right side
def partition(arr, l, r):
    element = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= element:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i


array = [2, 13, 8, 9, 5, 7, 4, 19]
size = len(array)
k = 3
print("Kth Smallest Element Optimal way is ", KthSmallestOptimal(array, 0, size - 1, k))
# Kth Smallest Element Optimal way is  5
