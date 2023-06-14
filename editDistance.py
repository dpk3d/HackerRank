"""
https://practice.geeksforgeeks.org/problems/edit-distance3702/1

Given two strings s and t. Return the minimum number of operations required to convert s to t.
The possible operations are permitted:

    Insert a character at any position of the string.
    Remove any character from the string.
    Replace any character from the string with any other character.

Example 1:

Input:
s = "geek", t = "gesek"
Output: 1
Explanation: One operation is required
inserting 's' between two 'e's of s.

Example 2:

Input :
s = "gfg", t = "gfg"
Output:
0
Explanation: Both strings are same.


Your Task:
You don't need to read or print anything.
Your task is to complete the function editDistance() which takes strings s and t as input parameters and
returns the minimum number of operation to convert the string s to string t.


Expected Time Complexity: O(|s|*|t|)
Expected Space Complexity: O(|s|*|t|)

"""


# Time Complexity: O(mn)
# Space Complexity: O(mn)
def editDistanceDP(str1, str2):
    m = len(str1)
    n = len(str2)
    # dp_array[x][y] : Minimum number of operation required to convert str1 -> str2
    dp_arr = [[0] * (n + 1) for _ in range(m + 1)]
    #   dp_arr[i][0] = x: transforming str1[0...x-1] into an empty string requires x deletions.
    #   dp_arr[0][j] = y: transforming an empty string into str2[0...y-1] requires y insertions.
    for x in range(1, m + 1):
        dp_arr[x][0] = x
    for y in range(1, n + 1):
        dp_arr[0][y] = y

    # If str1[i-1] == str2[j-1], then dp_arr[i][j] = dp_arr[i-1][j-1]. That is, no operation is required because the 
    # characters at positions i-1 and j-1 are already the same.

    for x in range(1, m + 1):
        for y in range(1, n + 1):
            if str1[x - 1] == str2[y - 1]:
                dp_arr[x][y] = dp_arr[x - 1][y - 1]
            else:
                dp_arr[x][y] = min(dp_arr[x - 1][y - 1], dp_arr[x - 1][y], dp_arr[x][y - 1]) + 1

    return dp_arr[m][n]


str1 = "geek"
str2 = "gesek"
print(" Minimum Number of edit distance : ",editDistanceDP(str1, str2))

#  Minimum Number of edit distance :  1
