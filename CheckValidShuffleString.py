"""
https://www.programiz.com/java-programming/examples/check-valid-shuffle-of-strings

Given strings A, B, and C, find whether C is formed by an interleaving of A and B.

An interleaving of two strings S and T is a configuration such that it creates a new string Y from the concatenation substrings of A and B and |Y| = |A + B| = |C|

For example:

A = "XYZ"
B = "ABC"

We can make multiple interleaving string Y like, XYZABC, XAYBCZ, AXBYZC, XYAZBC and many more
so here your task is to check whether you can create a string Y which can be equal to C.

Specifically, you just need to create substrings of string A and create substrings B and
concatenate them and check whether it is equal to C or not.

Note: a + b is the concatenation of strings a and b.

Return true if C is formed by an interleaving of A and B, else return false.

Example 1:

Input:
A = YX, B = X, C = XXY
Output: 0
Explanation: XXY is not interleaving
of YX and X

Example 2:

Input:
A = XY, B = X, C = XXY
Output: 1
Explanation: XXY is interleaving of
XY and X.
"""


# concat and sort mechanism
# it's a simple solution does not work for all test cases..
def validShuffle(inputString1, inputString2, shuffleString):
    concat_sort_str = sorted(inputString1 + inputString2)
    print(concat_sort_str)  # ['X', 'X', 'Y']
    sort_shuffle = sorted(shuffleString)
    print(sort_shuffle)  # ['X', 'X', 'Y']
    if sort_shuffle == concat_sort_str:
        print(" It's a Valid shuffle string : " + shuffleString)
        return True
    else:
        print(" Not valid shuffle string : " + shuffleString)
        return False


str1 = "XY"
str2 = "X"
checkStr = "XXY"
validShuffle(str1, str2, checkStr)


# It's a Valid shuffle string : XXY


def checkValidShuffle(i, j, k, a, b, c, dpArray):
    if i == len(a) and j == len(b) and k == len(c): return 1

    if dpArray[i][j] != -1: return dpArray[i][j]

    out1, out2 = 0, 0

    if i < len(a) and a[i] == c[k]:
        out1 = checkValidShuffle(i + 1, j, k + 1, a, b, c, dpArray)

    if j < len(b) and b[j] == c[k]:
        out2 = checkValidShuffle(i, j + 1, k + 1, a, b, c, dpArray)
    dpArray[i][j] = out1 + out2
    print(dpArray[i][j]) # print 0 or 1, or 2
    return dpArray[i][j]


# Dynamic Programming
def isInterleave(A, B, C):
    j = 0
    i = 0
    k = 0
    dpArray = [[-1 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
    print(dpArray) # [[-1, -1], [-1, -1], [-1, -1]]
    if len(A) + len(B) != len(C): return 0
    print(checkValidShuffle(i, j, k, A, B, C, dpArray)) # print 0 or 1
    return checkValidShuffle(i, j, k, A, B, C, dpArray)


str1 = "YX"
str2 = "X"
checkStr = "XXY"
isInterleave(str1, str2, checkStr)
