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
