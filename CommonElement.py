"""
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?

Example 1:

Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.


Your Task:
You don't need to read input or print anything. Your task is to complete the function commonElements() which take the 3 arrays A[], B[], C[] and their respective sizes n1, n2 and n3 as inputs and returns an array containing the common element present in all the 3 arrays in sorted order.
If there are no such elements return an empty array. In this case the output will be printed as -1.



Expected Time Complexity: O(n1 + n2 + n3)
Expected Auxiliary Space: O(n1 + n2 + n3)

https://practice.geeksforgeeks.org/problems/common-elements1132/1

"""
import sys


# We can perform intersection of two arrays keep the resulting array in temp and again perform intersection with 3rd array.

# Time complexity : O (arrlen1 + arrlen2 + arrlen3), Space Complexity : O(1)
def commonElementBruteForce(arr1, arr2, arr3):
    arrlen1 = len(arr1)
    arrlen2 = len(arr2)
    arrlen3 = len(arr3)
    a = b = c = 0
    while a < arrlen1 and b < arrlen2 and c < arrlen3:
        if arr1[a] == arr2[b] and arr2[b] == arr3[c]:
            print(" Common Element is : ", arr1[a])
            a += 1
            b += 1
            c += 1
        elif arr1[a] < arr2[b]:
            a += 1
        elif arr2[b] < arr3[c]:
            b += 1
        else:
            c += 1


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]

commonElementBruteForce(A, B, C)


# Handling duplicate, using previous element encountered
# Time complexity : O (arrlen1 + arrlen2 + arrlen3), Space Complexity : O(1)
def commonElementDuplicateHandling(arr1, arr2, arr3):
    arrlen1 = len(arr1)
    arrlen2 = len(arr2)
    arrlen3 = len(arr3)
    a = b = c = 0
    prev1 = prev2 = prev3 = - sys.maxsize - 1
    while a < arrlen1 and b < arrlen2 and c < arrlen3:

        # If arr1[a] = prev1 and a < arrlen1, keep incrementing a
        while arr1[a] == prev1 and a < arrlen1 - 1:
            a += 1

        # If arr2[b] = prev2 and b < arrlen2,keep incrementing b
        while arr2[b] == prev2 and b < arrlen2:
            b += 1

        # If arr3[c] = prev3 and c < arrlen3,keep incrementing c
        while arr3[c] == prev3 and c < arrlen3:
            c += 1
        # when common found update previous value
        if arr1[a] == arr2[b] and arr2[b] == arr3[c]:
            print(" Common Element is : ", arr1[a])
            prev1 = arr1[a]
            prev2 = arr2[b]
            prev3 = arr3[c]
            a += 1
            b += 1
            c += 1
        elif arr1[a] < arr2[b]:
            prev1 = arr1[a]
            a += 1
        elif arr2[b] < arr3[c]:
            prev2 = arr2[b]
            b += 1
        else:
            prev3 = arr3[c]
            c += 1


A = [1, 5, 10, 20, 40, 80]
B = [6, 7, 20, 80, 100]
C = [3, 4, 15, 20, 30, 70, 80, 120]
commonElementDuplicateHandling(A, B, C)
