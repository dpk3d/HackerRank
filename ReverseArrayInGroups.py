"""
Given an array arr[] of positive integers of size N. Reverse every sub-array group of size K.
"""


def reverseArrayInGroups(arr, N, K):
    initial = 0
    while initial < N:
        left = initial
        # Handling the case when arr is not multiple of K
        right = min(initial + K - 1, N - 1)
        while left < right:
            # Swapping the elements
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        initial += K


arr = [1, 42, 23, 14, 7, 8, 19, 10, 11, 4, 7]
k = 3
n = len(arr)
reverseArrayInGroups(arr, n, k)
print("Reversed  Array is ===", arr)
for x in range(0, n):
    print("Reversed Element Array is ===>", arr[x])

"""
Output:
Reversed Array is === [23, 42, 1, 8, 7, 14, 11, 10, 19, 7, 4]

Reversed Element Array is ===> 23
Reversed Element Array is ===> 42
Reversed Element Array is ===> 1
Reversed Element Array is ===> 8
Reversed Element Array is ===> 7
Reversed Element Array is ===> 14
Reversed Element Array is ===> 11
Reversed Element Array is ===> 10
Reversed Element Array is ===> 19
Reversed Element Array is ===> 7
Reversed Element Array is ===> 4
"""
