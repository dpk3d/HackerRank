"""

https://practice.geeksforgeeks.org/problems/next-permutation5226/1

Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater permutation of list of numbers.
 If such arrangement is not possible, it must be rearranged to the lowest possible order i.e. sorted in ascending order.
  You are given a list of numbers arr[ ] of size N.

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explanation: The next permutation of the
given array is {1, 2, 4, 3, 5, 6}.

Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explanation: As arr[] is the last
permutation. So, the next permutation
is the lowest one.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""


def nextPermutation(nums, n):
    l = len(nums)
    pivot = 0
    for x in range(l - 1, 0, -1):
        if nums[x - 1] < nums[x]:
            pivot = x
            break
    if pivot == 0:
        nums.sort()
        return
    swap = l - 1
    while nums[pivot - 1] >= nums[swap]:
        swap -= 1
    nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
    nums[pivot:] = reversed(nums[pivot:])


arr = [1, 2, 3, 6, 5, 4]
n = len(arr)
nextPermutation(arr, n)