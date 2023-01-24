"""
Move all negative numbers to beginning and positive to end with constant extra space.

An array contains both positive and negative numbers in random order.
Rearrange the array elements so that all negative numbers appear before all positive numbers.
"""


# Complexity O( n * log(n))
def easyWay(arr):
    arr.sort()
    print("Negative elements in beginning : ", arr)


array = [-3, 4, 60, -5, -8, -1, 10, 4, 5, 6, 6]
easyWay(array)


# Time complexity O(n) , Space - O(1)
def negativeFirst(arr):
    x = 0
    for y in range(0, len(arr)):
        if arr[y] < 0:
            temp = arr[y]
            arr[y] = arr[x]
            arr[x] = temp
            x = x + 1
    print("Negative elements in beginning :", arr)


array = [-3, 4, 60, -5, -8, -1, 10, 4, 5, 6, 6]
negativeFirst(array)


# Using Dutch National Flag Algorithm.
# Time complexity O(n) , Space - O(1)
def reArrange(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] < 0:
            start += 1
        elif arr[end] > 0:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]
    print("Negative elements Two Pointer Approach", arr)


array = [-3, 4, 60, -5, -8, -1, 10, 4, 5, 6, 6]
reArrange(array)
