"""
Find the maximum and minimum element in an array
"""


def minAndMax(arr):
    # Using built-in Functions
    print(" Minimum Array in the element is ", min(arr))
    print(" Maximum Array in the element is ", max(arr))


arr = [1, 23, 4, 5, -6, 5, 8, 34]
minAndMax(arr)


def minAndMax1(arr):
    minimum = maximum = arr[0]
    for x in range(1, len(arr)):
        if arr[x] > maximum:
            maximum = arr[x]
        if arr[x] < minimum:
            minimum = arr[x]
    print("Minimum and Maximum element in array via loop is : ", minimum, maximum)


arr = [1, 23, 4, 5, -6, 5, 8, 34]
minAndMax1(arr)


def minAndMax2(arr):
    arr.sort()
    print(" Minimum element via Sort is : ", arr[0])
    print(" Maximum element via Sort is : ", arr[-1])


arr = [1, 23, 4, 5, -6, 5, 8, 34]
minAndMax2(arr)


def minAndMax3(arr, low, high):
    minimum = arr[low]
    maximum = arr[high]

    # If given array has only one element
    if minimum == maximum:
        minimum = arr[low]
        maximum = arr[low]
        return (minimum, maximum)
    # when there is only two elements in array
    elif maximum == minimum + 1:
        if arr[low] > arr[high]:
            maximum = arr[low]
            minimum = arr[high]
        else:
            maximum = arr[high]
            minimum = arr[low]
        return (minimum, maximum)
    # When More than two elements
    else:
        mid = int((low + high) / 2)
        maximum1, minimum1 = minAndMax3(arr, low, mid)
        maximum2, minimum2 = minAndMax3(arr, mid + 1, high)

    return (max(maximum1, maximum2), min(minimum1, minimum2))


arr = [1020, 141, 45, 1, 90, 890]
high = len(arr) - 1
low = 0
arr_max, arr_min = minAndMax3(arr, low, high)
print('Minimum element is ', arr_min)
print('Maximum element is ', arr_max)
