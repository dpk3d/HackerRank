"""

https://leetcode.com/problems/search-a-2d-matrix/description/

You are given an m x n integer matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

"""


# Time - O(M*N) Space - O(1)
def searchMatrixBruteForce(matrix, target):
    return any(target in row for row in matrix)


matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 13
print("Element Found : ", searchMatrixBruteForce(matrix1, target1))


# Element Found :  False


# O(logM*logN) Using Binary Search
def searchMatrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    while top <= bottom:
        row = (top + bottom) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            break
    if not (top <= bottom):
        return False
    row = (top + bottom) // 2
    left, right = 0, cols - 1
    while left <= right:
        middle = (left + right) // 2
        if target < matrix[row][middle]:
            left = middle + 1
        elif target > matrix[row][middle]:
            right = middle - 1
        else:
            return True
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print("Element Found : ", searchMatrix(matrix, target))
# Element Found :  False
matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target1 = 13
print("Element Found : ", searchMatrix(matrix1, target1))
# Element Found :  False
