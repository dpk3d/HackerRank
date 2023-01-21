"""
Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

Example 1:

Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.

Example 2:

Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is [2, 3, 4, 5] which gives product as 120.

Your Task:
You don't need to read input or print anything. Your task is to complete the function maxProduct() which takes the array of integers array and n as parameters and returns an integer denoting the answer.
Note: Use 64-bit integer data type to avoid overflow.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 500
-102 ≤ Arri ≤ 102


"""


# Kadane's Algorithm , Time Complexity O(N) , Space - O(1)
def maxProductSubArray(arr):
    finalMax = prevMax = prevMin = arr[0]
    for x in arr[1:]:
        currentMin = min(prevMax * x, prevMin * x, x)
        currentMax = max(prevMax * x, prevMin * x, x)
        finalMax = max(finalMax, currentMax)
        prevMax = currentMax
        prevMin = currentMin
    return finalMax


arr = [6, -3, -10, 0, 2]
print(maxProductSubArray(arr))
