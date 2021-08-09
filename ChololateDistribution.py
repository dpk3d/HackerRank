"""

Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

Example 1:

Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.
Example 2:

Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}
Output: 2
Explanation: The minimum difference between
maximum chocolates and minimum chocolates
is 4 - 2 = 2 by choosing following M packets :
{3, 2, 4}.


"""


# Optimal solution of time complexity N log N

def getMinimumDiff(arr, n, m):
    # If array is empty or number of student is Zero.
    if (n == 0 or m == 0):
        return 0
    # Sorting the given packets
    arr.sort
    # When number of students are more than chocolate packet.
    if ( n < m ):
        return -1
    # Getting the ,difference
    diff = arr[ n - 1 ] - arr[0]

    # Moving through sub array to get minimum difference
    for x in range(len(arr) - m + 1):
        diff = min(diff, arr[x + m - 1], arr[x])
    return diff


ARRAY = [3, 4, 1, 9, 56, 7, 9, 12]
N = len(ARRAY)
M = 5

print("Minimum difference is", getMinimumDiff(ARRAY, N, M))

"""
Result:
Minimum difference is 1

"""
