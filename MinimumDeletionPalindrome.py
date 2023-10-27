"""
https://www.geeksforgeeks.org/minimum-number-deletions-make-string-palindrome/

Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome.

Note: The order of characters should be maintained.

Examples :

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string
Input : geeksforgeeks
Output : 8

"""


# Dynamic programming
# Time Complexity :  O(2n)
# Space Complexity :  O(2n)
def minimumNumberOfDeletions(input_str):
    # code here
    minDeletions(input_str, 0, len(input_str) - 1)
    print('The minimum number of deletions required is', minDeletions(X, 0, len(input_str) - 1))


def minDeletions(input_str, start, end):
    # Base Condition
    if start >= end:
        return 0
    # if the last character of the string is the same as the first character
    if input_str[start] == input_str[end]:
        return minDeletions(input_str, start + 1, end - 1)
    # 1. Remove the last character and recur for the remaining substring
    # 2. Remove the first character and recur for the remaining substring

    # return 1 (for remove operation) + minimum of the two values
    return 1 + min(
        minDeletions(input_str, start, end - 1),
        minDeletions(input_str, start + 1, end)
    )


X = "ACBCDBAA"
minimumNumberOfDeletions(X)


# Function to find out the minimum number of deletions required to
# convert a given string `X[i…j]` into a palindrome
def minDeletionsLookUp(X, i, j, lookup):
    # base condition
    if i >= j:
        return 0

    # construct a unique key from dynamic elements of the input
    key = (i, j)

    # if the subproblem is seen for the first time, solve it and store its result in a dictionary
    if key not in lookup:

        # if the last character of the string is the same as the first character
        if X[i] == X[j]:
            lookup[key] = minDeletionsLookUp(X, i + 1, j - 1, lookup)
        else:
            # if the last character of the string is different from the first character
            # 1. Remove the last character and recur for the remaining substring
            # 2. Remove the first character and recur for the remaining substring
            # return 1 (for remove operation) + minimum of the two values

            result = 1 + min(minDeletionsLookUp(X, i, j - 1, lookup),
                             minDeletionsLookUp(X, i + 1, j, lookup))
            lookup[key] = result

    # return the sub problem solution from the dictionary
    return lookup[key]


# create a dictionary to store solutions to sub problems
lookup = {}
X = "ACBCDBAA"
print('The minimum number of deletions required is : ', minDeletionsLookUp(X, 0, len(X) - 1, lookup))


def minimumNumberOfDeletions(S):
    # code here
    n = len(S)

    # Create a 2D array to store the minimum deletions required for subproblems
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
             # if the last character of the string is the same as the first character
            if S[i] == S[j]:
                # 1. Remove the last character and recur for the remaining substring
                dp[i][j] = dp[i + 1][j - 1]
            else:
                # 2. Remove the first character and recur for the remaining substring
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    # The minimum number of deletions to make a palindrome is stored in dp[0][n-1]
    return dp[0][n - 1]
input_str = "ACBCDBAA"
print('The minimum number of deletions required via DP is : ', minimumNumberOfDeletions(input_str))
