"""
https://leetcode.com/problems/add-digits/description/
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.



Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:

Input: num = 0
Output: 0



Constraints:

    0 <= num <= 231 - 1

"""


def addDigitsTillEnd(number):
    totalSum = 0
    while number > 0:
        reminder = number % 10
        totalSum += reminder
        number = number // 10
    if totalSum > 9:
        totalSum = addDigitsTillEnd(totalSum)
    return totalSum


print(addDigitsTillEnd(143))
# Result : 8
