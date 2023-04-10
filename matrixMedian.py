"""
https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1


Given a row wise sorted matrix of size R*C where R and C are always odd, find the median of the matrix.

Example 1:

Input:
R = 3, C = 3
M = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]
Output: 5
Explanation: Sorting matrix elements gives
us {1,2,3,3,5,6,6,9,9}. Hence, 5 is median.


Example 2:

Input:
R = 3, C = 1
M = [[1], [2], [3]]
Output: 2
Explanation: Sorting matrix elements gives
us {1,2,3}. Hence, 2 is median.

Your Task:
You don't need to read input or print anything. Your task is to complete the function median() which takes the integers R and C along with the 2D matrix as input parameters and returns the median of the matrix.

Expected Time Complexity: O(32 * R * log(C))
Expected Auxiliary Space: O(1)


Constraints:
1 <= R, C <= 400
1 <= matrix[i][j] <= 2000

"""

from bisect import bisect_right as upper_bound

MAX = 100;


def matrixMedianBinarySearch(matrix, rows, cols):
    median = matrix[0][0]
    max = 0
    for i in range(rows):
        if matrix[i][0] < median:
            median = matrix[i][0]
        if matrix[i][cols - 1] > max:
            max = matrix[i][cols - 1]

    desired = (rows * cols + 1) // 2

    while median < max:
        mid = median + (max - median) // 2
        place = [0];

        # count of elements smaller than or equal to mid
        for i in range(rows):
            j = upper_bound(matrix[i], mid)
            place[0] = place[0] + j
        if place[0] < desired:
            median = mid + 1
        else:
            max = mid
    return median


# Driver code
rows, cols = 3, 3

matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
print(" Median of the given matrix is : ",matrixMedianBinarySearch(matrix, rows, cols))
