"""
https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1
Given string str, find the length of the longest repeating subsequence such that it can be found twice in the given string.

The two identified subsequences A and B can use the same ith character from string str if and only if that ith character has different indices in A and B. For example, A = "xax" and B = "xax" then the index of first "x" must be different in the original string for A and B.

Example 1:

Input:
str = "axxzxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x z x y
0 1 2 3 4 5

The longest subsequence is "xx".
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str


subsequence B
x x
0 1  <-- index of subsequence B
------
2 4  <-- index of str

We are able to use character 'x'
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A
and index 0 in subsequence B.

Example 2:

Input:
str = "axxxy"
Output: 2
Explanation:
The given array with indexes looks like
a x x x y
0 1 2 3 4

The longest subsequence is "xx".
It appears twice as explained below.

subsequence A
x x
0 1  <-- index of subsequence A
------
1 2  <-- index of str


subsequence B
x x
0 1  <-- index of subsequence B
------
2 3  <-- index of str

We are able to use character 'x'
(at index 2 in str) in both subsequences
as it appears on index 1 in subsequence A
and index 0 in subsequence B.

"""


# Time Complexity: O(n2)
# Space Complexity : O(n2)
# Using Dynamic programming
def longestRepeatingSubSequence(inputString1):
    dynamicArray = [[0 for x in range(len(inputString1) + 1)] for y in range(len(inputString1) + 1)]
    print("generated dynamicArray : ", dynamicArray)
    # generated dynamicArray :  [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
    for rows in range(1, len(inputString1) + 1):
        for cols in range(1, len(inputString1) + 1):
            if inputString1[rows - 1] == inputString1[cols - 1] and rows != cols:
                dynamicArray[rows][cols] = 1 + dynamicArray[rows - 1][cols - 1]
            else:
                dynamicArray[rows][cols] = max(dynamicArray[rows][cols - 1], dynamicArray[rows - 1][cols])
    return dynamicArray[-1][-1]


str1 = "axxxy"
print("The Longest Repeating Subsequence is :", longestRepeatingSubSequence(str1))
# The Longest Repeating Subsequence is : 2


# Using Recursion
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

def longestRepeatingSubSequenceRecursion(inputString, l1, l2):
    if dp[l1][l2] != -1:
        return dp[l1][l2]

    # return if we have reached the end of either string
    if l1 == 0 or l2 == 0:
        dp[l1][l2] = 0
        return dp[l1][l2]

    # if characters at index m and n matches
    # and index is different
    if inputString[l1 - 1] == inputString[l2 - 1] and l1 != l2:
        dp[l1][l2] = longestRepeatingSubSequenceRecursion(inputString,
                                                          l1 - 1, l2 - 1) + 1

        return dp[l1][l2]

    # else if characters at index m and n don't match
    dp[l1][l2] = max(longestRepeatingSubSequenceRecursion(inputString, l1, l2 - 1),
                     longestRepeatingSubSequenceRecursion(inputString, l1 - 1, l2))
    return dp[l1][l2]


str = "axxxy"
m = len(str)

dp = [[-1 for i in range(1000)] for j in range(1000)]
print("The length of the largest subsequence that"
      " repeats itself is : "
      , longestRepeatingSubSequenceRecursion(str, m, m))
# The length of the largest subsequence that repeats itself is :  2


# Optimal Solution takes less space.
# Time Complexity: O(n2)
# Space Complexity: O(n)
def longestRepeatingSubSequenceOptimal(inputString):
    dynamicTable = [0 for _ in range(len(inputString) + 1)]
    for x in range(1, len(inputString) + 1):
        result = [0]
        for y in range(1, len(inputString) + 1):
            if inputString[x - 1] == inputString[y - 1] and x != y:
                result.append(1 + dynamicTable[y - 1])
            else:
                result.append(max(dynamicTable[y], result[-1]))
        dynamicTable = result[:]
        print("table is : ", dynamicTable)
        # table is: [0, 0, 0, 0, 0, 0]
        # table is: [0, 0, 0, 1, 1, 1]
        # table is: [0, 0, 1, 1, 2, 2]
        # table is: [0, 0, 1, 2, 2, 2]
        # table is: [0, 0, 1, 2, 2, 2]
    return dynamicTable[-1]


str1 = "axxxy"
print("The Longest Repeating Subsequence Optimal is :", longestRepeatingSubSequenceOptimal(str1))
# The Longest Repeating Subsequence Optimal is  : 2
