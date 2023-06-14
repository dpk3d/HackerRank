"""
https://practice.geeksforgeeks.org/problems/longest-prefix-suffix2527/1
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

NOTE: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Example 1:

Input: s = "abab"
Output: 2
Explanation: "ab" is the longest proper
prefix and suffix.

Example 2:

Input: s = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper
prefix and suffix.

"""


def longest_prefix_suffix(str):
    n = len(str)
    for res in range(n // 2, 0, -1):
        # Check for shorter lengths of first half.
        prefix = str[0: res]
        suffix = str[n - res: n]
        if prefix == suffix:
            return res

    # if no prefix and suffix match occurs
    return 0


print("Longest Prefix and suffix is : ", longest_prefix_suffix("abab"))


# Longest Prefix and suffix is :  2


def longest_prefix_suffix_1(s):
    n = len(s)

    if n == 0:
        return 0

    # end_suffix and end_prefix are used to keep track of the common suffix and prefix respectively.
    # For the prefix we search only in first half of string (0-->n//2-1) since
    # suffix and prefix do not overlap.
    end_suffix = n - 1
    end_prefix = n // 2 - 1

    # Traverse each character of suffix from end to start and check for a match of prefix
    # in first half of array.
    while end_prefix >= 0:
        if s[end_prefix] != s[end_suffix]:
            if end_suffix != n - 1:
                end_suffix = n - 1  # reset end_suffix
            else:
                end_prefix -= 1
        else:
            end_suffix -= 1
            end_prefix -= 1

    # The longest common suffix and prefix is s[end+1:]
    return n - end_suffix - 1


print("Longest Prefix and suffix is : ", longest_prefix_suffix_1("abab"))
# Longest Prefix and suffix is :  2
