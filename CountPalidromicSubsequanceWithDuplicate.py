"""
https://practice.geeksforgeeks.org/problems/count-palindromic-subsequences/1

Given a string str of length N, you have to find number of palindromic subsequence
 (need not necessarily be distinct) present in the string str.
Note: You have to return the answer module 109+7;


Example 1:

Input:
Str = "abcd"
Output:
4
Explanation:
palindromic subsequence are : "a" ,"b", "c" ,"d"

Example 2:

Input:
Str = "aab"
Output:
4
Explanation:
palindromic subsequence are :"a", "a", "b", "aa"
"""


# Time Complexity :  O(n*n)
# Space Complexity :  O(n*n)
# Using DP
def count_palindromic_sub_sequence(input_string):
    str_len = len(input_string)
    dp_arr = [[0] * str_len for _ in range(str_len)]
    for x in range(str_len):
        for y in range(x, -1, -1):
            if x == y:
                dp_arr[y][x] = 1
            else:
                if input_string[x] == input_string[y]:
                    dp_arr[y][x] = dp_arr[y + 1][x] + dp_arr[y][x - 1] + 1
                else:
                    dp_arr[y][x] = dp_arr[y + 1][x] + dp_arr[y][x - 1] - dp_arr[y + 1][x - 1]
    return dp_arr[0][str_len - 1] % (10 ** 9 + 7)


print("Count for Palindromic Subsequence is : ", count_palindromic_sub_sequence("abcd"))
# Count for Palindromic Subsequence is :  4
