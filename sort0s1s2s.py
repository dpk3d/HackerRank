"""Given an array of size N containing only 0s, 1s, and 2s;
 sort the array in ascending order."""


# Time Complexity O(N) , Space O(1)
def sort(arr, length):
    low = 0
    mid = 0
    high = length - 1

    while mid <= high:
        if arr[mid] == 0:
            # Swapping
            arr[low], arr[mid] = arr[mid], arr[low]
            # Increment by 1
            low = low + 1
            mid = mid + 1
        elif arr[mid] == 1:
            # Increment by 1
            mid = mid + 1
        else:
            # Swapping
            arr[mid], arr[high] = arr[high], arr[mid]
            high = high - 1
    return arr


arr = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2]
size = len(arr)
print("Sorted array of 0s 1s 2s are ==>", sort(arr, size))
"""
Output is :
Sorted array of 0s 1s 2s are ==> [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
"""



# Time Complexity O(N) , Space O(1)
def sort0s1s2s(deepak, length):
    zeros = 0
    one = 0
    two = 0
    for x in range(length):
        if deepak[x] == 0:
            zeros += 1
        elif deepak[x] == 1:
            one += 1
        elif deepak[x] == 2:
            two += 1
    x = 0
    while zeros > 0:
        deepak[x] = 0
        x += 1
        zeros -= 1
    while one > 0:
        deepak[x] = 1
        x += 1
        one -= 1
    while two > 0:
        deepak[x] = 2
        x += 1
        two -= 1
    print(printArray(deepak))


def printArray(arr):
    print("New Sorted Array", arr)


deepak = [0, 1, 2, 0, 1, 2, 0, 1, 2, 1, 2, 0, 1, 2]
size = len(deepak)
sort0s1s2s(arr, size)
"""
Output is :
New Sorted Array [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
"""
