"""

Rearrange array in alternating positive & negative items with O(1) extra space

https://www.geeksforgeeks.org/rearrange-array-alternating-positive-negative-items-o1-extra-space/

Given an array of positive and negative numbers, arrange them in an alternate fashion such that every positive
number is followed by a negative and vice-versa maintaining the order of appearance. The number of positive and
negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there
are more negative numbers, they too appear at the end of the array.

"""


def rotateArray(arr, length, outOfPlace, curr):
    temp = arr[curr]
    for x in range(curr, outOfPlace, -1):
        arr[x] = arr[x - 1]
    arr[outOfPlace] = temp
    return arr

# Time Complexity is : O(N * N) , Space is : O(1)
def reArrangePositiveNegative(arr, length):
    outOfPlace = -1
    for index in range(length):
        if outOfPlace >= 0:
            # if element at outOfPlace place is negative and if element at index is positive we can rotate the array
            # to right or if element at outOfPlace place in positive and if element at index is negative we can
            # rotate the array to right
            if arr[index] >= 0 and arr[outOfPlace] < 0 or arr[index] < 0 and arr[outOfPlace] >= 0:
                arr = rotateArray(arr, length, outOfPlace, index)
                if (index - outOfPlace) > 2:
                    outOfPlace += 2
                else:
                    outOfPlace -= 1
        if outOfPlace == -1:
            # A[index] to be in out of place
            if ((arr[index] >= 0 and index % 2 == 0) or
                    (arr[index] < 0 and index % 2 == 1)):
                outOfPlace = index
    return arr


arr = [-5, -2, 5, 2, 4,7, 1, 8, 0, -8]
n = len(arr)
print("Rearranged Elements : ",reArrangePositiveNegative(arr,n))