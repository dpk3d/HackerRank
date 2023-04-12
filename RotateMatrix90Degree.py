"""
https://www.geeksforgeeks.org/rotate-a-matrix-by-90-degree-in-clockwise-direction-without-using-any-extra-space/

Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Examples:

Input:
1 2 3
4 5 6
7 8 9
Output:
7 4 1
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2

"""
from typing import List


# Time Complexity :  (n^2+n)/2 => O(n^2)
# Space Complexity :  O(1)
def rotate90Degree(matrix: List[List[int]]):
    length = len(matrix)
    x = 0
    y = 0
    # transpose
    while x < length and y < length + 1:
        if y != length:
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]
            y += 1
        else:
            x += 1
            y = x
            if y == length:
                y += 1

    for z in range(length):
        matrix[z] = matrix[z][::-1]

    print("Rotated Matrix by 90 degree is : ", matrix)
    # Rotated Matrix by 90 degree is  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


givenMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate90Degree(givenMatrix)


# Time Complexity : O(n^2)
# Space Complexity : O(1)
def rotateUsingReverse(matrix):
    matrix.reverse()
    for x in range(len(matrix)):
        for y in range(x + 1, len(matrix[x])):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    print("Rotated Matrix by 90 degree with reverse is ", matrix)
    # Rotated Matrix by 90 degree with reverse is  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


givenMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateUsingReverse(givenMatrix)


# Time Complexity : O(n^2)
# Space Complexity : O(1)
def rotateWithoutReverse(matrix):
    start = 0
    length = len(matrix) - 1
    while start < length:
        matrix[start], matrix[length] = matrix[length], matrix[start]
        start += 1
        length -= 1
    # transpose
    for x in range(len(matrix)):
        for y in range(x):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]

    print("Rotated Matrix without Reverse is : ", matrix)
    # Rotated Matrix without Reverse is :  [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


givenMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateWithoutReverse(givenMatrix)
