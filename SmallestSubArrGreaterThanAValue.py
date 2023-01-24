"""
https://practice.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x/0

Given an array of integers (A[])  and a number x, find the smallest subarray with sum greater than the given value.

Note: The answer always exists. It is guaranteed that x doesn't exceed the summation of a[i] (from 1 to N).

Example 1:

Input:
A[] = {1, 4, 45, 6, 0, 19} , x  =  51
Output: 3
Explanation: Minimum length subarray is {4, 45, 6}

Example 2:

Input:
A[] = {1, 10, 5, 2, 7} , x  = 9
Output: 1
Explanation: Minimum length subarray is {10}

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N, x ≤ 105
1 ≤ A[] ≤ 104
"""
from past.builtins import xrange


# Time Complexity O(N^2) , Space Complexity O(1)
def minimumSubArrayBruteForce(arr, x):
    length = len(arr)
    min_length = length + 1
    for i in range(0, length):
        total = arr[i]
        if total > x:
            return 1
        for j in range(i + 1, length):
            total += arr[j]
            if total > x and (j - i + 1) < min_length:
                min_length = (j - i + 1)
    return min_length


Array = [1, 4, 45, 6, 0, 19]
X = 51
print("Smallest Sub Array Length is :  ", minimumSubArrayBruteForce(Array, X))


# Time Complexity :  O(N)
def optimalMinimumSubArrLength(arr, x):
    # Going from left to right , total tracks the running sum.
    total = left = right = 0
    # It is the same idea as initializing result as float("inf"). We know the index range will never exceed len(array),
    # so initializing result as len(array)+1 will be sufficient enough.
    result = len(arr) + 1
    # If sum is less than X right moves forward one step, else left moves forward one step.
    while right < len(arr):
        total += arr[right]
        while total > x: # while total >= x: --> will change the output to 5.
            result = min(result, right - left + 1)
            total -= arr[left]
            left += 1
        right += 1
    return result if result <= len(arr) else 0


arr = [3, 1, 2, 4, 5]
sum = 15
print("Smallest Sub Array Length is :  ", optimalMinimumSubArrLength(arr, sum))


# Time complexity : - O(N)
def minSubArrForLoop(nums, s):
    l = sum = 0
    res = len(nums) + 1
    for i in xrange(len(nums)):
        sum += nums[i]
        while sum > s:
            res = min(res, i - l + 1)
            sum -= nums[l]
            l += 1
    return res if res <= len(nums) else 0


arr = [1, 10, 5, 2, 7]
target = 9
print("Smallest Sub Array Length is :  ", minSubArrForLoop(arr, target))
