"""
Given an array arr of N integers, write a function that returns true if there is a triplet (a, b, c)
that satisfies a2 + b2 = c2, otherwise false.
"""


# Brute Force Approach, It has time complexity of n * n * n
def checkTripplet(arr, n):
    i = 0

    for x in range(n - 2):
        for y in range(i + 1, n):
            for z in range(x + 1, n - 1):
                a = arr[x] * arr[x]
                b = arr[y] * arr[y]
                c = arr[z] * arr[z]
                if a == b + c or b == c + a or c == b + a:
                    return 1
    return 0


# Input Array
array = [1, 3, 6, 4, 5]
size = len(array)

if checkTripplet(array, size):
    print("Yes  The Given Array has Pythagorean Triplets")
else:
    print("No ")


# Optimal Approach, having complexity of n * n .
# Get Square of each element in Array ---> O(n), We sort the array first ---> n log n

def optimalTriplet(arr, n):
    # Square of each element
    for x in range(n):
        arr[x] = arr[x] * arr[x]

    # Sorting the array
    arr.sort()
    # Pick one element and search for other two.
    for x in range(n - 1, 1, -1):
        # a and b two index variable from each end of array iterating towards themselves
        y = 0
        z = x - 1
        while (z < y):
            if (arr[z] + arr[y] == arr[x]):
                return True
            else:
                if (arr[z] + arr[y] < arr[x]):
                    y = y + 1
                else:
                    z = z - 1
    return False


array1 = [3, 8, 4, 6, 5]
size = len(array1)
if optimalTriplet(array1, size):
    print("Yes  Optimal : Given Array has Pythagorean Triplets")
else:
    print("No The Given Array is not triplets")
