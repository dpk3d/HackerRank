"""
https://practice.geeksforgeeks.org/problems/palindromic-array-1587115620/1
Given an Integer array A[] of n elements. Your task is to complete the function PalinArray. Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

Example 1:

Input:
5
111 222 333 444 555

Output:
1

Explanation:
A[0] = 111 //which is a palindrome number.
A[1] = 222 //which is a palindrome number.
A[2] = 333 //which is a palindrome number.
A[3] = 444 //which is a palindrome number.
A[4] = 555 //which is a palindrome number.
As all numbers are palindrome so This will return 1.

Example 2:

Input:
3
121 131 20

Output:
0

Explanation:
20 is not a palindrome hence the output is 0.

Constraints:
1 <=T<= 50
1 <=n<= 20
1 <=A[]<= 10000


"""


# Time Complexity: O(n)
# Auxiliary Space: O(1)

def minOperation(arr, length):
    minimumCount = 0
    x, y = 0, length - 1  # Two Pointers
    while x < y:
        if arr[x] == arr[y]:  # First and last element same
            x += 1
            y -= 1
        elif arr[x] > arr[y]:  # Left element is greater merge two right one's
            y -= 1
            arr[y] += arr[y + 1]
            minimumCount += 1
        else:  # merge two left one's
            x += 1
            arr[x] += arr[x + 1]
            minimumCount += 1

    return minimumCount


arr = [1, 4, 5, 9, 1]
n = len(arr)
print("Count of minimum operations is " + str(minOperation(arr, n)))
# Count of minimum operations is 2
