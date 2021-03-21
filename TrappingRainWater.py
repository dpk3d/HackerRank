"""
Given an array arr[] of N non-negative integers representing the height of blocks.
If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season.
"""


# Time Complexity  = O(n) + O(n) + O(n) Equivalent to O(n), Space Complexity O(n) + O(n)
def trapping_water(arr):
    size = len(arr)
    left = size * [0]
    right = size * [0]
    trapped_water = 0
    # Initializing first value of array in Left
    left[0] = arr[0]
    # Initializing Maximum sum is first element in the beginning
    maximum_so_far_left = arr[0]

    for index in range(0, size):
        if maximum_so_far_left < arr[index]:
            maximum_so_far_left = arr[index]
            left[index] = maximum_so_far_left
        else:
            left[index] = maximum_so_far_left

    # Initializing Maximum sum as last element of Array
    maximum_so_far_right = arr[-1]

    for index in range(size - 1, -1, -1):
        if maximum_so_far_right < arr[index]:
            maximum_so_far_right = arr[index]
            right[index] = maximum_so_far_right
        else:
            right[index] = maximum_so_far_right

    for i in range(0, size):
        trapped_water = trapped_water + min(left[i], right[i]) - arr[i]
    return trapped_water


array = [3, 0, 0, 2, 0, 4]
print("Trapped Water is :", trapping_water(array))
# Trapped Water is : 10



# Optimal Solution : Time Complexity : O(n), Space Complexity : O(1)
# Taking Two Pointer Left and Right in same array to achieve space complexity O(1)
def trapping_water_optimal(arr):
    size = len(arr)
    left = 0
    right = size - 1
    left_maximum = 0
    right_maximum = 0
    trapped_water = 0
    while left <= right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_maximum:
                left_maximum = arr[left]
            else:
                trapped_water += left_maximum - arr[left]
                left += 1
        else:
            if arr[right] >= right_maximum:
                right_maximum = arr[right]
            else:
                trapped_water += right_maximum - arr[right]
                right -= 1
    return trapped_water


array = [3, 0, 0, 2, 0, 4]
print("Trapped Water Optimal way is :", trapping_water(array))
# Trapped Water Optimal way is : 10
