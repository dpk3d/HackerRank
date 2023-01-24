"""
https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1

Given an array arr of n positive integers and a number k.
One can apply a swap operation on the array any number of times,
i.e choose any two index i and j (i < j) and swap arr[i] , arr[j] .
Find the minimum number of swaps required to bring all the numbers less than or equal to k together,
 i.e. make them a contiguous subarray.

Example 1:

Input :
arr[ ] = {2, 1, 5, 6, 3}
K = 3
Output :
1
Explanation:
To bring elements 2, 1, 3 together,
swap index 2 with 4 (0-based indexing),
i.e. element arr[2] = 5 with arr[4] = 3
such that final array will be-
arr[] = {2, 1, 3, 6, 5}


Example 2:

Input :
arr[ ] = {2, 7, 9, 5, 8, 7, 4}
K = 6
Output :
2
Explanation:
To bring elements 2, 5, 4 together,
swap index 0 with 2 (0-based indexing)
and index 4 with 6 (0-based indexing)
such that final array will be-
arr[] = {9, 7, 2, 5, 4, 7, 8}

"""


def minSwap(arr, n, k):
    # Find count of elements
    # which are less than
    # equals to k
    count = 0
    for i in range(0, n):
        if (arr[i] <= k):
            count = count + 1

    # Find unwanted elements
    # in current window of
    # size 'count'
    bad = 0
    for i in range(0, count):
        if (arr[i] > k):
            bad = bad + 1

    # Initialize answer with
    # 'bad' value of current
    # window
    ans = bad
    j = count
    for i in range(0, n):

        if (j == n):
            break

        # Decrement count of
        # previous window
        if (arr[i] > k):
            bad = bad - 1

        # Increment count of
        # current window
        if (arr[j] > k):
            bad = bad + 1

        # Update ans if count
        # of 'bad' is less in
        # current window
        ans = min(ans, bad)

        j = j + 1

    return ans


# Driver code
arr = [2, 1, 5, 6, 3]
n = len(arr)
k = 3
print(minSwap(arr, n, k))

arr1 = [2, 7, 9, 5, 8, 7, 4]
n = len(arr1)
k = 5
print(minSwap(arr1, n, k))
