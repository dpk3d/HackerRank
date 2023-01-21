"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

https://leetcode.com/problems/longest-substring-without-repeating-characters/

"""

from collections import deque


# Using DEQUE , Brute Force
def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    dq = deque()
    for character in s:
        while character in dq:
            dq.popleft()
        dq.append(character)
        if len(dq) > max_length:
            max_length = len(dq)
    return max_length


s = "deeepakkk"
print("Length of Longest Substring is  : ", lengthOfLongestSubstring(s))
"""
Length of Longest Substring is  :  4
"""


# Complexity of O(n)
def lengthOfLongestSubstring1(s):
    start = end = max_length = 0

    while end < len(s):
        # print(" value 1 ", s[start:end])
        if s[end] not in s[start:end]:
            # print("value 2 ", s[end])
            max_length = max(max_length, len(s[start:end + 1]))
            # print("max lenght is " , max_length)
            end += 1
        else:
            start = s[start:end].index(s[end]) + start + 1
            # print( " start  is  , ", start)
    return max_length


s = "madamdeemadamedee"
print("Length of Longest Substring is  : ", lengthOfLongestSubstring1(s))
"""
Output: 
Length of Longest Substring is  :  4
"""


# Complexity can reach to O(n)
def lengthOfLongestSubstring2(s: str) -> int:
    max_length = 0
    current_string = ""
    for character in s:
        while character in current_string:
            # print(" character is : ", character)
            current_string = current_string[1::]
            # print(" current string is : ", current_string)
        current_string = current_string + character
        # print(" new current string : ", current_string)
        max_length = max(max_length, len(current_string))
    return max_length


s = "deeepakkk"
lengthOfLongestSubstring2(s)
print("Length of Longest Substring is  : ", lengthOfLongestSubstring2(s))
"""
Output: 
Length of Longest Substring is  :  4
"""


# Using Set
def lengthOfLongestSubstring3(s) -> int:
    max_length = 0
    character_set = set()
    start_delete_index = 0
    for index, character in enumerate(s):
        while character in character_set:
            character_set.remove(s[start_delete_index])
            start_delete_index += 1
        character_set.add(character)
        if len(character_set) > max_length:
            max_length = len(character_set)
    return max_length


s = "deeepakkk"
lengthOfLongestSubstring2(s)
print("Length of Longest Substring is  : ", lengthOfLongestSubstring2(s))
"""
Output: 
Length of Longest Substring is  :  4
"""
