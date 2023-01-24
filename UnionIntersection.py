"""
Find the Union and intersection of two sorted arrays.
"""


# Brute force approach , search each element of arr1 into arr2
def intersection(arr1, arr2):
    result = []
    for x in arr1:
        if x not in result and x in arr2:
            result.append(x)
    return result


arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
print(" Intersection of two arrays : ", intersection(arr1, arr2))


# Using Set
def intersectionSet(arr1, arr2):
    return set(arr1) & set(arr2)


arr1 = [7, 1, 5, 2, 3, 8, 9, 6]
arr2 = [3, 8, 6, 20, 8, 5, 7]
print(" Intersection of two arrays, Set : ", intersectionSet(arr1, arr2))


# Using two pointer approach Time Complexity - O(l1 + l2) , Space - O(1)
def intersectionTwoPointer(arr1, arr2, l1, l2):
    i, j = 0, 0
    while i < l1 and j < l2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            print(arr2[j], end="\n")
            j += 1
            i += 1


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
l1 = len(arr1)
l2 = len(arr2)
intersectionTwoPointer(arr1, arr2, l1, l2)


def union(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1
        else:
            print(arr2[j], end=" ")
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i], end=" ")
        i += 1

    while j < n:
        print(arr2[j], end=" ")
        j += 1


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
m = len(arr1)
n = len(arr2)
union(arr1, arr2, m, n)


# union of two sorted arrays (Handling Duplicates)
def union_array(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0

    # keep track of last element to avoid duplicates
    prev = None

    while i < m and j < n:
        if arr1[i] < arr2[j]:
            if arr1[i] != prev:
                print(arr1[i], end='\n')
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != prev:
                print(arr2[j], end='\n')
                prev = arr2[j]
            j += 1
        else:
            if arr1[i] != prev:
                print(arr1[i], end='\n')
                prev = arr1[i]
            i += 1
            j += 1

    while i < m:
        if arr1[i] != prev:
            print(arr1[i], end='\n')
            prev = arr1[i]
        i += 1

    while j < n:
        if arr2[j] != prev:
            print(arr2[j], end='\n')
            prev = arr2[j]
        j += 1


arr1 = [7, 1, 5, 2, 3, 8, 9, 6]
arr2 = [3, 8, 6, 20, 8, 5, 7]
union_array(arr1, arr2)
