"""
https://practice.geeksforgeeks.org/problems/sorted-matrix2333/1

Given an NxN matrix Mat. Sort all elements of the matrix.

Example 1:

Input:
N=4
Mat=[[10,20,30,40],
[15,25,35,45]
[27,29,37,48]
[32,33,39,50]]
Output:
10 15 20 25
27 29 30 32
33 35 37 39
40 45 48 50
Explanation:
Sorting the matrix gives this result.

Example 2:

Input:
N=3
Mat=[[1,5,3],[2,8,7],[4,6,9]]
Output:
1 2 3
4 5 6
7 8 9
Explanation:
Sorting the matrix gives this result.

Your Task:
You don't need to read input or print anything. Your task is to complete the function sortedMatrix() which takes the integer N and the matrix Mat as input parameters and returns the sorted matrix.

Expected Time Complexity:O(N2LogN)
Expected Auxillary Space:O(N2)


Constraints:
1<=N<=1000
1<=Mat[i][j]<=105

"""


# Using Vector
#  Time Complexity : O(n2log2n).
#  O(n*n) for traversing, and O(n2log2n) for sorting the vector
#  Space Complexity : O(n*n), For vector.

def sortMatrix(matrix):
    length = len(matrix)
    resultVector = []
    for x in range(length):
        for y in range(length):
            resultVector.append(matrix[x][y])
    resultVector.sort()
    z = 0
    for i in range(length):
        for j in range(length):
            matrix[i][j] = resultVector[z]
            z += 1
    print(matrix)
    return matrix
    # Sorted Matrix is [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


givenMatrix = [[1, 5, 3], [2, 8, 7], [4, 6, 9]]
sortMatrix(givenMatrix)


# Using Merge K sort Array Mechanism
# Time Complexity of Merge : O(n log(n))
# Space Complexity of Merge is : O(n)
def mergeKSortedArrays(matrix):
    import heapq
    output = []
    minHeap = []
    for x in range(len(matrix)):
        heapq.heappush(minHeap, (matrix[x][0], x, 0))
        # loop to merge all
    while minHeap:
        val, row, col = heapq.heappop(minHeap)
        output.append(val)
        if col + 1 < len(matrix[row]):
            heapq.heappush(minHeap, (matrix[row][col + 1], row, col + 1))
    print(output)
    # [1, 2, 4, 5, 3, 6, 8, 7, 9]
    return output


givenMatrix = [[1, 5, 3], [2, 8, 7], [4, 6, 9]]
mergeKSortedArrays(givenMatrix)


def sortMatrixWithReduce(matrix):
    from functools import reduce
    length_of_sublist = len(matrix[0])
    sorted_list = iter(sorted(reduce(lambda x, y: x + y, matrix), reverse=True))
    print(list(zip(*[sorted_list] * length_of_sublist)))
    # Sorted Matrix using Reduce : [(45, 43, 42, 41), (30, 29, 21, 20), (19, 17, 16, 10), (4, 3, 2, 1)]


givenMatrix = [[41, 45, 20, 21], [1, 2, 3, 4], [30, 42, 43, 29], [16, 17, 19, 10]]
sortMatrixWithReduce(givenMatrix)
