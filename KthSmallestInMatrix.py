"""
https://practice.geeksforgeeks.org/problems/kth-element-in-matrix/1

Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Example 1:

Input:
N = 4
mat[][] =     {{16, 28, 60, 64},
                   {22, 41, 63, 91},
                   {27, 50, 87, 93},
                   {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.

Example 2:

Input:
N = 4
mat[][] =     {{10, 20, 30, 40}
                   {15, 25, 35, 45}
                   {24, 29, 37, 48}
                   {32, 33, 39, 50}}
K = 7
Output: 30
Explanation: 30 is the 7th smallest element.

Your Task:
You don't need to read input or print anything.
Complete the function kthsmallest() which takes the mat, N and K as input parameters and returns the kth smallest element in the matrix.

Expected Time Complexity: O(K*Log(N))
Expected Auxiliary Space: O(N)

Constraints:
1 <= N <= 50
1 <= mat[][] <= 10000
1 <= K <= N*N

"""


# Time complexity: O(n*n)
#  Space complexity: O(n)

def kthSmallestBruteForce(matrix, k):
    arr = []
    for row in matrix:
        for col in row:
            arr.append(col)
    arr.sort()
    # print(arr[k - 1])
    # Kth Smallest element is 27
    return arr[k - 1]


K = 3
givenMatrix = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
print("Kth Smallest element in matrix with Brute force is : ", kthSmallestBruteForce(givenMatrix, K))


# Kth Smallest element in matrix with Brute force is :  27


# Using Max Heap to keep upto k elements
# Time Complexity : O(n*n)
# Space Complexity : O(k)
def kthSmallestEasy(matrix, k):
    from heapq import heappush
    from heapq import heappop
    row, col = len(matrix), len(matrix[0])
    maxHeap = []
    for x in range(row):
        for y in range(col):
            heappush(maxHeap, -matrix[x][y])
            if len(maxHeap) > k:
                heappop(maxHeap)
    return -heappop(maxHeap)


K = 3
givenMatrix = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
print("Kth Smallest number using Max Heap is : ", kthSmallestEasy(givenMatrix, K))


# Kth Smallest number using Max Heap is :  27


# Since matrix rows are sorted we need to find the smallest from rows only
# Time Complexity : O(K * logK)
# Space Complexity : O(K)
def kthSmallestUsingMeanHeap(matrix, k):
    from heapq import heappush
    from heapq import heappop
    row, col = len(matrix), len(matrix[0])
    minHeap = []  # value, a, b
    for x in range(min(k, row)):
        heappush(minHeap, (matrix[x][0], x, 0))
    output = 0
    for y in range(k):
        output, a, b = heappop(minHeap)
        if b + 1 < col:
            heappush(minHeap, (matrix[a][b + 1], a, b + 1))
    return output


K = 3
givenMatrix = [[16, 28, 60, 64], [22, 41, 63, 91], [27, 50, 87, 93], [36, 78, 87, 94]]
print("Kth Smallest number using Min Heap is : ", kthSmallestUsingMeanHeap(givenMatrix, K))
# Kth Smallest number using Min Heap is :  27
