"""
Given a sorted array of positive integers.
Your task is to rearrange  the array elements alternatively i.e first element should be max value,
second should be min value, third should be second max, fourth should be second min and so on.
"""


# Time Complexity O(n) , Space Complexity O(n)
def simpleRearrangeAlternate(arr, n):
    minimum_element = 0
    maximum_element = n - 1
    result = n * [None]

    # To indicate whether we need to copy remaining largest or remaining smallest at next position
    flag = True
    for x in range(n):
        if flag is True:
            result[x] = arr[maximum_element]
            maximum_element -= 1
        else:
            result[x] = arr[minimum_element]
            minimum_element += 1
        flag = bool(1 - flag)
    # Copy result[] to arr[]
    for x in range(n):
        arr[x] = result[x]
    return arr


arr = [1, 2, 3, 4, 7, 8, 9, 10]
print("Actual Array", arr)
print("Re Arranged Array", simpleRearrangeAlternate(arr, 8))


# Best Optimal solution of Time Complexity O(n) , Space Complexity O(1)
def optimalReArrangeAlternate(arr, n):
    largest_index = n - 1
    smallest_index = 0
    maximum_element = arr[largest_index] + 1
    for x in range(n):
        if (x % 2 == 0):
            arr[x] = (arr[largest_index] % maximum_element) * maximum_element + arr[x]
            largest_index -= 1
        else:
            arr[x] = (arr[smallest_index] % maximum_element) * maximum_element + arr[x]
            smallest_index += 1
    # Re arranged Array
    for x in range(n):
        arr[x] = arr[x] // maximum_element
    return arr


arr = [1, 2, 3, 4, 7, 8, 9, 10, 11, 12, 14, 17, 20]
print("Input Array", arr)
print("Output Array", optimalReArrangeAlternate(arr, 13))
