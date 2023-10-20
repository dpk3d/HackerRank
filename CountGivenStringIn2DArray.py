"""
https://www.geeksforgeeks.org/find-count-number-given-string-present-2d-character-array/


Given a 2-Dimensional character array and a string, we need to find the given string in 2-dimensional character array, such that individual characters can be present left to right, right to left, top to down or down to top.

Examples:

Input : a ={
            {D,D,D,G,D,D},
            {B,B,D,E,B,S},
            {B,S,K,E,B,K},
            {D,D,D,D,D,E},
            {D,D,D,D,D,E},
            {D,D,D,D,D,G}
           }
        str= "GEEKS"
Output :2

Input : a = {
            {B,B,M,B,B,B},
            {C,B,A,B,B,B},
            {I,B,G,B,B,B},
            {G,B,I,B,B,B},
            {A,B,C,B,B,B},
            {M,C,I,G,A,M}
            }
        str= "MAGIC"

Output :4

"""


# Time Complexity O(m x n) ^2
# Space Complexity O(m x n)
def internalSearch(index, inputString, row, col, arrStr,
                   row_max, col_max):
    found = 0
    if (0 <= row <= row_max and
            0 <= col <= col_max and
            inputString[index] == arrStr[row][col]):
        match = inputString[index]
        index += 1
        arrStr[row][col] = 0
        if index == len(inputString):
            found = 1
        else:
            # through Backtrack searching in every direction
            found += internalSearch(index, inputString, row,
                                    col + 1, arrStr, row_max, col_max)
            found += internalSearch(index, inputString, row,
                                    col - 1, arrStr, row_max, col_max)
            found += internalSearch(index, inputString, row + 1,
                                    col, arrStr, row_max, col_max)
            found += internalSearch(index, inputString, row - 1,
                                    col, arrStr, row_max, col_max)
        arrStr[row][col] = match
    return found


# Function to search the string in 2d array
def searchString(inputString, row, col, strr,row_count, col_count):
    found = 0
    for r in range(row_count):
        for c in range(col_count):
            found += internalSearch(0, inputString, r, c,
                                    strr, row_count - 1, col_count - 1)

    return found


# Driver code

inputString = "MAGIC"
inputArray = ["BBABBM", "CBMBBA", "IBABBG",
              "GOZBBI", "ABBBBC", "MCIGAM"]

strr = [0] * len(inputArray)

for i in range(len(inputArray)):
    strr[i] = list(inputArray[i])

print("count: ", searchString(inputString, 0, 0, strr,
                              len(strr), len(strr[0])))
