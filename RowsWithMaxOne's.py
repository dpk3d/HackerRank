"""

https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1

Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

Example 1:

Input:
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).

Example 2:

Input:
N = 2, M = 2
Arr[][] = {{0, 0}, {1, 1}}
Output: 1
Explanation: Row 1 contains 2 1's (0-based
indexing).

Your Task:
You don't need to read input or print anything. Your task is to complete the function rowWithMax1s() which takes the array of booleans arr[][], n and m as input parameters and returns the 0-based index of the first row that has the most number of 1s. If no such row exists, return -1.

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N, M ≤ 103
0 ≤ Arr[i][j] ≤ 1

"""


# Row wise Linear Search
# Time Complexity : O(rows * cols), Space Complexity : O(1)
def bruteForce(rows, cols, matrix):
    max1Count = 0
    maxRowIndex = 0
    for x in range(rows):
        row1Count = 0
        for y in range(cols):
            if matrix[x][y] == 1:
                row1Count = row1Count + 1
        if row1Count > max1Count:
            max1Count = row1Count
            maxRowIndex = x

    return maxRowIndex


rows = 4
cols = 4
matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

print(" Rows with Maximum one's is :", bruteForce(rows, cols, matrix), "index")


#  Rows with Maximum one's is : 2 index


# Using Binary Search O(nlogm)
# Time Complexity : O(NlogM) , Space Complexity : O(logN)
def maxOneBinarySearch(matrix, rows, cols):
    max1Count = 0
    maxRowIndex = 0
    for x in range(rows):
        firstOneIndex = binarySearch(matrix[x], 0, cols - 1)
        rowsOneCount = cols - firstOneIndex
        if firstOneIndex != -1 and rowsOneCount > max1Count:
            max1Count = rowsOneCount
            maxRowIndex = x
    return maxRowIndex


def binarySearch(matrix, left, right):
    if left <= right:
        mid = left + (right - left) // 2
        if matrix[mid - 1] == 0 or mid == 0 and matrix[mid] == 1:
            return mid
        elif matrix[mid] == 0:
            return binarySearch(matrix, mid + 1, right)
        else:
            return binarySearch(matrix, left, mid - 1)
    return -1


rows = 4
cols = 4
matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

print(" Rows with Maximum one's via Binary Search is :", maxOneBinarySearch(matrix, rows, cols), "index")
# Rows with Maximum one's via Binary Search is : 2 index


# Optimal Solution
# Time Complexity : O(N+M) , Space Complexity : O(1)
# From Top Right corner to bottom left
def optimalMaxOnesInRow(matrix, rows, cols):
    maxRowIndex = -1
    presentCol = cols - 1
    for x in range(rows):
        while presentCol >= 0 and matrix[x][presentCol] == 1:
            presentCol = presentCol - 1
            maxRowIndex = x

    return maxRowIndex


rows = 4
cols = 4
matrix = [[0, 1, 1, 1],
          [0, 0, 1, 1],
          [1, 1, 1, 1],
          [0, 0, 0, 0]]

print(" Rows with Maximum one's Optimal way : ", optimalMaxOnesInRow(matrix, rows, cols), "index")
#  Rows with Maximum one's A Optimal way :  2 index
