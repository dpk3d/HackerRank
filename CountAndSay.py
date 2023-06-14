"""
https://leetcode.com/problems/count-and-say/

The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.

To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit.
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

For example, the saying and conversion for digit string "3322251":

Given a positive integer n, return the nth term of the count-and-say sequence.


Example 1:

Input: n = 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: n = 4
Output: "1211"
Explanation:
countAndSay(1) = "1"
countAndSay(2) = say "1" = one 1 = "11"
countAndSay(3) = say "11" = two 1's = "21"
countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"

"""
from itertools import groupby


# Time Complexity : O(N * M)
# Space Complexity : O(N * M)
def countAndSay(N):
    if N == 1:
        return "1"
    if N == 2:
        return "11"
    startString = "11"
    for x in range(2, N):
        count = 1
        newString = ""
        for y in range(len(startString)):
            if y == len(startString) - 1:
                newString = newString + str(count) + startString[y]
                break
            if startString[y] == startString[y + 1]:
                count += 1
            else:
                newString = newString + str(count) + startString[y]
                count = 1
        startString = newString
    return newString


print("Generated String is : ", countAndSay(6))
# Generated String is :  312211

# Time Complexity : O(N * N)
def countAndSayRecursive(N):
    if N == 1:
        return "1"
    last = countAndSayRecursive(N - 1)
    N = len(last)
    result = ""
    count = 1
    for x in range(N):
        if x == N - 1 or last[x] != last[x + 1]:
            result += str(count) + last[x]
            count = 1
        else:
            count += 1

    return result


print("Generated String via Recursive approach : ", countAndSayRecursive(6))
# Generated String via Recursive approach :  312211

#     Time:   O(2^n)
#     Memory: O(2^n)
def countAndSayElegant(N):
    if N == 1:
        return "1"
    return getCount(countAndSayElegant(N - 1))

def getCount(N):
    return ''.join(f'{sum(1 for _ in group)}{key}' for key, group in groupby(N))


print("Generated String via Elegant Recursive approach : ", countAndSayElegant(6))
# Generated String via Elegant Recursive approach :  312211

def countAndSayDP(N):
    dynamicProgram = ["" for x in range(0, N + 1)]  # ['', '', '', '', '', '', '']
    dynamicProgram[1] = "1 "
    x = 2
    while x < N + 1:
        print(f'x:{x} dynamicProgram[{x - 1}]:{dynamicProgram[x - 1]}')
        # x:2 dynamicProgram[1]:1
        # x:3 dynamicProgram[2]:11
        # x:4 dynamicProgram[3]:21
        # x:5 dynamicProgram[4]:1211
        # x:6 dynamicProgram[5]:111221
        # x:7 dynamicProgram[6]:312211
        # x:8 dynamicProgram[7]:13112221
        # x:9 dynamicProgram[8]:1113213211
        count = 0
        for y in range(0, len(dynamicProgram[x - 1]) - 1):
            if dynamicProgram[x - 1][y] == dynamicProgram[x - 1][y + 1]:
                count += 1
            else:
                dynamicProgram[x] += chr(count + 1 + ord('0')) + dynamicProgram[x - 1][y]
                count = 0
        dynamicProgram[x] += ' '
        x += 1
    return dynamicProgram[-1][:-1]


print("Generated String via Elegant Recursive approach : ", countAndSayDP(9))
# Generated String via Elegant Recursive approach :  31131211131221
