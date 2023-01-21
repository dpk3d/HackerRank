"""
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""


# Dynamic Programing way
def longestPalindromicSubStr(inputString):
    longestPalindrome = ""
    pair = [[0] * len(inputString) for _ in range(len(inputString))]
    # print("pair values are : ", pair)
    for x in range(len(inputString)):
        pair[x][x] = True
        longestPalindrome = inputString[x]
        # print(longestPalindrome)
    for x in range(len(inputString) - 1, -1, -1):
        for y in range(x + 1, len(inputString)):
            # print(" x: %d , y: %d" % (x, y))
            if inputString[x] == inputString[y]:
                if y - x == 1 or pair[x + 1][y - 1] is True:
                    pair[x][y] = True
                    if len(longestPalindrome) < len(inputString[x:y + 1]):
                        longestPalindrome = inputString[x:y + 1]
                        # print(longestPalindrome)
    return longestPalindrome


s = "madamdeemadamedee"
print("Longest Substring in Given String is : ", longestPalindromicSubStr(s))


def longestPalindrome(s) -> str:
    result = ""
    result_length = 0
    for i in range(len(s)):
        # odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > result_length:
                result_length = (right - left + 1)
                result = s[left:right + 1]
            left -= 1
            right += 1
        # even length
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > result_length:
                result_length = (right - left + 1)
                result = s[left:right + 1]
            left -= 1
            right += 1
    return result

s = "madamdeemadamedee"
print("Longest Substring in Given String is : ", longestPalindrome(s))
