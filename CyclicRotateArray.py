"""
https://leetcode.com/problems/rotate-array/
https://practice.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1
Given an array, rotate the array by one position in clock-wise direction.

"""


def rotate( nums, k):
    arr = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]
    for i, val in enumerate(arr):
        nums[i] = val
    return arr

nums = [2,3,3,5,6,9,0]
print("Cyclic Rotation by 1 : ",rotate(nums, 1))


def rotate1(nums ,k):
    def reverse(a, l, h):
        if l >= h:
            return
        temp = a[l]
        a[l] = a[h]
        a[h] = temp
        reverse(a, l + 1, h - 1)

    if k > len(nums):
        k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


nums = [2,3,3,5,6,9,0]
print("Cyclic Rotation by 3 : ",rotate(nums, 3))