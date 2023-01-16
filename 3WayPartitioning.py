"""
https://practice.geeksforgeeks.org/problems/three-way-partitioning/1

Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to return the modified array.

Example 1:

Input:
n = 5, A[] = {1, 2, 3, 3, 4}
[a, b] = [1, 2]
Output: 1
Explanation: One possible arrangement is:
{1, 2, 3, 3, 4}. If you return a valid
arrangement, output will be 1.


Example 2:

Input:
n = 3
A[] = {1, 2, 3}
[a, b] = [1, 3]
Output: 1
Explanation: One possible arrangement
is: {1, 2, 3}. If you return a valid
arrangement, output will be 1.


Your Task:
You don't need to read input or print anything. The task is to complete the function threeWayPartition() which takes the array[], a and b as input parameters and modifies the array in-place according to the given conditions.
Note: The generated output is 1 if you modify the given array successfully.


Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

"""


# Two Pointer, Swapping variables
def threeWayPartitioning(array, length, a, b):
    startingElement = 0
    endingElement = length - 1
    x = 0
    while x <= a:
        if array[x] < startingElement:
            array[x], array[startingElement] = array[startingElement], array[x]
            x += 1
            startingElement += 1
        elif array[x] > b:
            array[x], array[endingElement] = array[endingElement], array[x]
            endingElement -= 1
        else:
            x += 1


arr = [1, 2, 3, 3, 4]
#arr = [87, 78, 16, 94]
n = len(arr)
#threeWayPartitioning(arr, n, 37, 72)
threeWayPartitioning(arr, n, 1, 2)

print("Modified array")
for i in range(n):
    print(arr[i], end=" ")
