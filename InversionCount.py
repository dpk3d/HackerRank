"""
Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted.
If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then
the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
"""


############################################################################
def SimpleInversionCount(arr):
    count = 0
    for x in range(len(arr)):
        for y in range(x + 1, len(arr)):
            if arr[x] > arr[y]:
                count += 1
    return count


arr = [2, 0, 4, 3, 9, 8, 9, 7, 10]
print("Inversion count is ==>", SimpleInversionCount(arr))
############################################################################


def InversionCountMergeSort(input_arr, n):
    # A resulting_arr is temporary array to store sorted array of merge func.
    resulting_arr = [0] * n
    return mergeSort(input_arr, resulting_arr, 0, n - 1)


# This Function will use MergeSort to count inversions
def mergeSort(input_arr, resulting_arr, left, right):
    inversion_count = 0

    # Making recursive call only if more than one elements are there
    if left < right:
        # mid is dividing array into 2 sub arrays
        mid = (left + right) // 2

        # Calculating inversion counts in the left sub array
        inversion_count += mergeSort(input_arr, resulting_arr, left, mid)

        # Calculating inversion counts in right sub array
        inversion_count += mergeSort(input_arr, resulting_arr, mid + 1, right)

        # Merge 2 sub arrays into a sorted one
        inversion_count += final_merge(input_arr, resulting_arr, left, mid, right)
    return inversion_count


# Merge two sub arrays into a single sorted sub array
def final_merge(input_arr, resulting_arr, left, mid, right):
    a = left
    b = mid + 1
    c = left
    inv_count = 0

    # No Inversion here
    while a <= mid and b <= right:
        if input_arr[a] <= input_arr[b]:
            resulting_arr[c] = input_arr[a]
            c += 1
            a += 1
        else:
            # Inversion
            resulting_arr[c] = input_arr[b]
            inv_count += (mid - a + 1)
            c += 1
            b += 1
    # Copying remaining array to left sub array
    while a <= mid:
        resulting_arr[c] = input_arr[a]
        c += 1
        a += 1
    #  Copying remaining array to right sub array
    while b <= right:
        resulting_arr[c] = input_arr[b]
        c += 1
        b += 1

    # Copying the sorted array into final array
    for x in range(left, right + 1):
        input_arr[x] = resulting_arr[x]

    return inv_count


arr = [1, 3, 4, 8, 20, 0, 11, 20, 6, 4, 5]
n = len(arr)
result = InversionCountMergeSort(arr, n)
print("Number of inversions are", result)
