"""
https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1
"""


def minimiseMaxDiff(arr, k, n):
    arr.sort()
    maxDiff = arr[n-1] - arr[0]
    smallest = arr[0] + k
    largest = arr[ n - 1] - k

    for x in range(1,n):
        small = min(smallest, arr[x] - k)
        big = max(largest, arr[x] + k)
        maxDiff = min(maxDiff, big - small)
    return maxDiff


k = 2
arr = [1, 5, 8, 12, 22, 40, 10]
n = len(arr)
print(" Minimise difference is  : ", minimiseMaxDiff(arr, k, n))


def minimiseMaximumDifference(arr, k):
    length = len(arr)
    result = []
    for x in arr:
        if x < k:
            result.append(x + k)
        else:
            result.append(x - k)
    result.sort()
    height = result[-1] - result[0]
    return height


k = 2
arr = [1, 5, 8, 12, 22, 40, 10]
print(" Minimise difference is  : ", minimiseMaximumDifference(arr, k))
