"""
Given two arrays X and Y of positive integers, find the number of pairs such that
xy > yx (raised to power of) where x is an element from X and y is an element from Y.
"""


# Time Complexity O( n * m )
def simpleApproach(arr1, len1, arr2, len2):
    pairs = 0
    for a in range(len1):
        for b in range(len2):
            if pow(arr1[a], arr2[b]) > pow(arr2[b], arr1[a]):
                print("Pairs are ===>", arr1[a], arr2[b])
                pairs += 1
    return pairs


arr1 = [2, 1, 6]
arr2 = [1, 5]
print("Number of Pairs count ==>", simpleApproach(arr1, 3, arr2, 2))

# Need to work on this, This will handle corner cases and execptions
def binarySearchToGetIndex(arr, n, element):
    low = 0
    high = n - 1
    pairs = -1
    while low <= high:
        mid = low + high // 2
        if arr[mid] > element:
            pairs = mid
            high = mid - 1
        else:
            low = mid + 1
    print("Pairs  === >>", pairs)
    return pairs


# Time Complexity O ( n + m)
# To Handle Exception and corner cases , need to call binarySearchToGetIndex method in below method.
def numberOfPairs(deepArray, moniArray, deepLength, moniLength):
    zeros = 0
    one = 0
    two = 0
    three = 0
    four = 0
    deepArray.sort()
    moniArray.sort()
    for x in range(moniLength):
        if moniArray[x] == 0:
            zeros += 1
        if moniArray[x] == 1:
            one += 1
        if moniArray[x] == 2:
            two += 1
        if moniArray[x] == 3:
            three += 1
        if moniArray[x] == 0:
            four += 1
    # Traversing in First Array
    pairs = 0
    for x in range(deepLength):
        if deepArray[x] == 0:
            continue
        elif deepArray[x] == 1:
            pairs += 1
        elif deepArray[x] == 2:
            pairs += one + zeros
            pairs -= three
            pairs -= four
        else:
            pairs += one + zeros

    return pairs


deepArray = [2, 1, 6, 8, 9, 0, 10, 11]
moniArray = [1, 5, 0, 13, 2, 7, 9, 98]
print("Number of Pairs count 2nd Approach ==>", numberOfPairs(deepArray, moniArray, 8, 8))

"""
Output:
Pairs are ===> 2 1
Pairs are ===> 2 5
Pairs are ===> 6 1
Number of Pairs count ==> 3
Number of Pairs count 2nd Approach ==> 12
"""
