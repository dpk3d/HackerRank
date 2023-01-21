"""
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

"""


# Using Sorting Algorithm like Merge Sort and Heap Sort .
# Time Complexity is O (n long n)
def KthLargestEasyMethod(arr, k):
    arr.sort()
    # return array[k - 1] , Gives the Kth Smallest Element
    return arr[-k]


array = [2, 13, 8, 9, 5, 7, 4, 19]
k = 3
print("Kth Largest Element via sorting algorithm : ", KthLargestEasyMethod(array, k))



# Complexity - Time - O(nlogk) - Space - O(k)
import heapq

from past.builtins import xrange


def KthLargestPQ(arr, k):
    priorityQueue = arr[:k]
    heapq.heapify(priorityQueue)
    for i in arr[k:]:
        heapq.heappush(priorityQueue, i)
        heapq.heappop(priorityQueue)
    return priorityQueue[0]


arr = [3, 2, 1, 5, 6, 4]
k = 2

print(" Kth Largest Element via Priority Queue is : ", KthLargestPQ(arr, k))


# Time complexity O(n)- average , worst case is O(N^2)
def partition(arr, left, right):
    pivot = arr[right]  # Picking last element as pivot
    i = left
    # going from left to right - 1
    for j in xrange(left, right):
        # larger element is in left side
        if arr[j] > pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[right], arr[i] = arr[i], arr[right]  # swapping i and last element
    return i


def quickSelect(arr, start, n, k):
    position = partition(arr, start, n)
    if position == k - 1:
        return arr[position]
    elif position >= k:
        return quickSelect(arr, start, position - 1, k)
    return quickSelect(arr, position + 1, n, k)


def findKthLargest(arr, k):
    return quickSelect(arr, 0, len(arr) - 1, k)


arr = [3, 2, 1, 5, 9, -1, 6, 4]
k = 2

print(" Kth Largest Element via Quick Select : ", KthLargestPQ(arr, k))
