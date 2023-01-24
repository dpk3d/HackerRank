"""
Given an array of positive and negative numbers, find if there is a subarray (of size at least one) with 0 sum.

Examples:

    Input: {4, 2, -3, 1, 6}
    Output: true
    Explanation:
    There is a subarray with zero sum from index 1 to 3.

    Input: {4, 2, 0, 1, 6}
    Output: true
    Explanation: The third element is zero. A single element is also a sub-array.

    Input: {-3, 2, 3, 1, 6}
    Output: false

https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

"""


# Time Complexity O(N) , Space O(N)
def subArraySumBrute(arr):
    sum = 0
    s = set()
    for x in range(len(arr)):
        sum += arr[x]
        if sum == 0 or sum in s:
            return True
        s.add(sum)
    return False


arr = [4, 2, -3, 1, 6]
print(subArraySumBrute(arr))
