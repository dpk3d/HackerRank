"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for array = [1,2,3], the following are all the permutations of array: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of array = [1,2,3] is [1,3,2].
    Similarly, the next permutation of array = [2,3,1] is [3,1,2].
    While the next permutation of array = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.
"""


def nextPermutation(nums):
    l = len(nums)
    pivot = 0
    for x in range(l-1, 0, -1):
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
    return nums


arr = [1, 3, 5, 4, 3, 2, 1]
print(" Next Permutation for nums is : ", nextPermutation(arr))
