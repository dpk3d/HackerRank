"""
Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m.
Task is to check whether a2[] is a subset of a1[] or not.
Both the arrays can be sorted or unsorted.

Example 1:

Input:
a1[] = {11, 1, 13, 21, 3, 7}
a2[] = {11, 3, 7, 1}
Output:
Yes
Explanation:
a2[] is a subset of a1[]

Example 2:

Input:
a1[] = {1, 2, 3, 4, 5, 6}
a2[] = {1, 2, 4}
Output:
Yes
Explanation:
a2[] is a subset of a1[]


Example 3:

Input:
a1[] = {10, 5, 2, 23, 19}
a2[] = {19, 5, 3}
Output:
No
Explanation:
a2[] is not a subset of a1[]

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)
"""


# Time Complexity  - O( N * N ) , Space Complexity - O(1)
def checkSubsetBruteForce(arr1, arr2):
    x = 0
    y = 0
    for x in range(len(arr1)):
        for y in range(len(arr2)):
            if arr1[x] == arr2[y]:
                break
        if y == len(arr2):
            return 0
    return 1


array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 2, 3]
print(" Result : ", checkSubsetBruteForce(array1, array2))


# Time Complexity O(N) , Space Complexity  O(N)
def checkSubsetOptimal(arr1, arr2):
    s = set()
    for x in range(len(arr1)):
        s.add(arr1[x])
    if s.issuperset(arr2):
        return "Yes"
    return "No"


array1 = [1, 2, 3, 4, 5, 6]
array2 = [1, 2, 9]
print(" Result : ", checkSubsetOptimal(array1, array2))
