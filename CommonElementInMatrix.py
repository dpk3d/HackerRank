"""
https://www.geeksforgeeks.org/common-elements-in-all-rows-of-a-given-matrix/


"""


# Brute Force Approach is to consider every element and check if it's present in all rows.
# Little Optimal Solution is to sort all matrix rows, and then use hashing . Time Complexity : O(mnlogn)

# Optimal Solution Using Map.
# Time Complexity : O(m * n)
# Space Complexity : O(N)
def commonElement(matrix, numberOfRows, numberOfCols):
    map = dict()
    for y in range(numberOfCols):
        map[(matrix[0][y])] = 1  # Assigning default value as 1
    for x in range(1, numberOfRows):
        for y in range(numberOfCols):
            if ((matrix[x][y]) in map.keys() and map[(matrix[x][y])] == x):
                map[(matrix[x][y])] = x + 1
                if x == numberOfRows - 1:
                    print(matrix[x][y], end=" ")


givenMatrix = [[1, 2, 1, 4, 8],
               [3, 7, 8, 5, 1],
               [8, 7, 7, 3, 1],
               [8, 1, 2, 7, 9],
               ]
commonElement(givenMatrix, 4, 5)
