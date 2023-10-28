"""
https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
banner

Consider a rat placed at (0, 0) in a square matrix of order N * N.
It has to reach the destination at (N - 1, N - 1).
 Find all possible paths that the rat can take to reach from source to destination.
 The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right).
  Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1},
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at
(3, 3) from (0, 0) by two paths - DRDDRR
and DDRDRR, when printed in sorted order
we get DDRDRR DRDDRR.

"""
from self import self

# Backtracking
# DOing using Recursion
# Time Complexity : O(4^(m*n))
# Space Complexity :  O(m*n)

"""
    Start at the source(0,0) with an empty string and try every possible path i.e upwards(U), downwards(D), leftwards(L) and rightwards(R).
    As the answer should be in lexicographical order so it’s better to try the directions in lexicographical order i.e (D,L,R,U)
    Declare a 2D-array named visited because the question states that a single cell should be included only once in the path
    ,so it’s important to keep track of the visited cells in a particular path.
    If a cell is in path, mark it in the visited array.
    Also keep a check of the “out of bound” conditions while going in a particular direction in the matrix. 
    Whenever you reach the destination(n,n) it’s very important to get back as shown in the recursion tree.
    While getting back, keep on unmarking the visited array for the respective direction.
    Also check whether there is a different path possible while getting back and if yes, then mark that cell in the visited array.

"""


# Recursion program
def solve(row, col, empty_str, arr, n, visited, answer):
    if 0 <= row < n and 0 <= col < n:
        if arr[row][col] == 1 and visited[row][col] == 0:
            visited[row][col] = 1
            if row == col == n - 1:
                answer.append(empty_str)
            solve(row + 1, col, empty_str + 'D', arr, n, visited, answer)
            solve(row, col - 1, empty_str + 'L', arr, n, visited, answer)
            solve(row - 1, col, empty_str + 'U', arr, n, visited, answer)
            solve(row, col + 1, empty_str + 'R', arr, n, visited, answer)
            visited[row][col] = 0


def findPath(m, n):
    visited = [[0] * n for i in range(n)]
    answer = []
    empty_str = ''
    solve(0, 0, empty_str, m, n, visited, answer)
    return answer


n = 4
m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
print(" The Path for rat is : ", findPath(m, n))
#  The Path for rat is :  ['DDRDRR', 'DRDDRR']
