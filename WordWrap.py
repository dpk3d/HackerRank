"""

https://practice.geeksforgeeks.org/problems/word-wrap1646/1

Given an array nums[] of size n, where nums[i] denotes the number of characters in one word.
Let K be the limit on the number of characters that can be put in one line (line width).
Put line breaks in the given sequence such that the lines are printed neatly.
Assume that the length of each word is smaller than the line width.
When line breaks are inserted there is a possibility that extra spaces are present in each line.
 The extra spaces include spaces put at the end of every line except the last one.

You have to minimize the following total cost where total cost = Sum of cost of all lines,
 where cost of line is = (Number of extra spaces in the line)2.

Example 1:

Input: nums = {3,2,2,5}, k = 6
Output: 10
Explanation: Given a line can have 6
characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4
So total cost = (6-3)2 + (6-2-2-1)2 = 32+12 = 10.
As in the first line word length = 3 thus
extra spaces = 6 - 3 = 3 and in the second line
there are two word of length 2 and there already
1 space between two word thus extra spaces
= 6 - 2 -2 -1 = 1. As mentioned in the problem
description there will be no extra spaces in
the last line. Placing first and second word
in first line and third word on second line
would take a cost of 02 + 42 = 16 (zero spaces
on first line and 6-2 = 4 spaces on second),
which isn't the minimum possible cost.

Example 2:

Input: nums = {3,2,2}, k = 4
Output: 5
Explanation: Given a line can have 4
characters,
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 2
Line number 3: From word no. 3 to 3
Same explaination as above total cost
= (4 - 3)2 + (4 - 2)2 = 5.


Your Task:
You don't need to read or print anything.
 Your task is to complete the function solveWordWrap()
  which takes nums and k as input parameter and returns the minimized total cost.


Expected Time Complexity: O(n2)
Expected Space Complexity: O(n)
"""


# Time Complexity: O(n2)
# Space Complexity: O(1) constant time

def word_wrap_best(nums, n, k):
    # initialize total cost
    total_cost = 0
    for i in range(n - 2):
        # size of window left after the current element
        size = k - 1 - nums[i]
        # cost of current line
        sum = k - nums[i]
        while (size >= 0):
            size = size - nums[i + 1] - 1
            # breaks immediately
            if (size < 0):
                break
            sum = sum - nums[i] - 1
            i = i + 1

        # add current cost to total cost
        total_cost = total_cost + (sum * sum)
    return total_cost


nums = [3, 2, 2, 5]
n = len(nums)
k = 6
print("Total Cost for word wrap is : ", word_wrap_best(nums, n, k))
# Total Cost for word wrap is :  10



# --------------------------------------------------------------------------------------

# This is little different in terms of output
import sys


# Time Complexity : O(n2)
# Space Complexity : O(n)
# Space Optimised solve using Dynamic programming
def optimal_word_wrap(arr, n, k):
    dp_array = [0] * n
    # result[x] store index of last word in line starting with word arr[x].
    result = [0] * n

    # If only one word is there then just one line required and cost is zero
    # Ending point is n - 1
    dp_array[n - 1] = 0
    result[n - 1] = n - 1

    # Iterating over each index in the array
    for x in range(n - 2, -1, -1):
        curr_len = -1
        dp_array[x] = sys.maxsize
        # Adding words in current line
        for y in range(x, n):
            # Update characters in current line. arr[y] is the characters in current word
            # 1 represents space character between two words.
            curr_len += (arr[y] + 1)
            # If limit is violated then break
            if curr_len > k:
                break
            # If current word added to the line is last word then cost is zero
            if y == n - 1:
                cost = 0
            else:
                # Else cost is square of extra space + line breaks in the rest of words
                cost = ((k - curr_len) *
                        (k - curr_len) + dp_array[y + 1])

            # Checking if we get the minimum cost
            if cost < dp_array[x]:
                dp_array[x] = cost
                result[x] = y

    # Print starting index and ending index of words present in each line.
    x = 0
    while x < n:
        print(x + 1, result[x] + 1, end=" ")
        x = result[x] + 1


array = [3, 2, 2, 5]
n = len(array)
K = 6
optimal_word_wrap(array, n, K)

# Input will consist of array of integers where each array element represents length of each word of string. For
# example, for string S = "Geeks for Geeks", input array will be arr[] = {5, 3, 5}. Output consists of a series of
# integers where two consecutive integers represent starting word and ending word of each line.

# 1 1 2 3 4 4
