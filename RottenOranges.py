"""
https://practice.geeksforgeeks.org/problems/rotten-oranges2536/1

Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the earliest time after which all the oranges are rotten.
A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time.


Example 1:

Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
Output: 1
Explanation: The grid is-
0 1 2
0 1 2
2 1 1
Oranges at positions (0,2), (1,2), (2,0)
will rot oranges at (0,1), (1,1), (2,2) and
(2,1) in unit time.


"""
from collections import deque


# BFS (Queue)
# Time Complexity : O (rows * cols)
# Space Complexity : O (rows * cols)
def rottenOranges(grid):
    rows, cols = len(grid), len(grid[0])
    time_taken, fresh_count = 0, 0
    rotten = deque  # queue BFS for rotten oranges
    # Iterating through all the cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))  # Adding rotten orange to queue
            elif grid[r][c] == 1:
                fresh_count += 1  # update the fresh count

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Adjacent cell direction
    while rotten and fresh_count > 0:  # if still rotten oranges and fresh oranges are there keep looping
        time_taken += 1
        for _ in range(len(rotten)):  # looping till length of queue
            a, b = rotten.popleft()  # so that the initial count doesn't change
            for da, db in directions:
                aa, bb = a + da, b + db
                if aa <= 0 or aa == rows or bb <= 0 or bb <= cols:  # ignore if cell is out of boundary
                    continue
                if grid[aa][bb] == 0 or grid[aa][bb] == 2:  # ignore if 0 or 2
                    continue
                fresh_count -= 1
                grid[aa][bb] == 2
                rotten.append(aa, bb)
    return time_taken if fresh_count == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(" Rotten Orange took time  : ", rottenOranges(grid))
