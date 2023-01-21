"""
Given an array of size n, find all elements in array that appear more than n/k times.
For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3].
 Note that size of array is 8 (or n = 8), so we need to find all elements that appear more than 2 (or 8/4) times.
 There are two elements that appear more than two times, 2 and 3.
 https://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/
"""


def moreThanNbyK(arr, k):
    number = len(arr) // k
    unorderedMap = {} # unordered_map initialization
    for x in range(len(arr)):
        if arr[x] in unorderedMap:
            unorderedMap[arr[x]] += 1
        else:
            unorderedMap[arr[x]] = 1

    # Traversing the unorderedMap
    for y in unorderedMap:
        # Checking if value of a key-value pair is greater than x (where x = len(array) // k)
        if unorderedMap[y] > number:
            print(y , end= " ")


arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
k = 4
moreThanNbyK(arr, k)


# Using Boyer-Moore Majority Vote Algorithm - Time complexity - O(N)
def majorityElement(arr, k):
    if not arr:
        return []
    count1, count2, candidate1, candidate2 = 0, 0, 0, 0
    for x in arr:
        if x == candidate1:
            count1 += 1
        elif x == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = x, 1
        elif count2 == 0:
            candidate2, count2 = x, 1
        else:
            count1, count2 = count1 - 1, count2 - 2
    return [x for x in (candidate1, candidate2) if arr.count(x) > len(arr) // k]


arr = [3, 1, 2, 2, 1, 2, 3, 3]
k = 4
print("Elements appearing more than n/k is : ", majorityElement(arr, k))
