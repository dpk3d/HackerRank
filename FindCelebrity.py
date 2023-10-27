"""
https://www.geeksforgeeks.org/the-celebrity-problem/


    If A knows B, then A can’t be a celebrity. Discard A, and B may be celebrity.
    If A doesn’t know B, then B can’t be a celebrity. Discard B, and A may be celebrity.
    Repeat above two steps till there is only one person.
    Ensure the remained person is a celebrity. (What is the need of this step?)

"""
from self import self


# Using Elimination Technique : STACK
# Time Complexity :  O(N)
# Space Complexity : O(1)
def knows(a, b):
    pass


def findCelebrity(self, N):
    candidate = 0
    for x in range(1, N):
        # Assuming know API is already provided
        if knows(candidate, x):
            candidate = x
    is_celebrity(candidate)
    return - 1


def is_celebrity(self, i):
    for j in range(self.N):
        if i == j:
            if knows(i, j) or not knows(j, i):
                return False
    return True


M = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]

findCelebrity(self, M)


# Time Complexity : O(N)
# Space Complexity : O(1)
def celebrity(matrix, n):
    r = 0
    for i in range(1, n):
        # checking if r th person knows i th person
        if matrix[r][i] == 1:
            matrix[r][r] = 1
            r = i
        else:
            matrix[i][i] = 1

    for i in range(n):
        # checking if i th person can be a celebrity or not
        if matrix[i][i] == 0:
            flag = 0
            # iterating in the i th column to check whether everyone knows i th person or not
            for j in range(n):
                # checking if matrix[j][i] is not a diagonal element and if j th person knows i th person
                if j != i and matrix[j][i] == 0:
                    flag = 1
                    break
            if flag == 0:
                return i

    return -1


M = [[0, 0, 1, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0]]
celebrity(M, 4)
