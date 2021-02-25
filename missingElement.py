"""
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N.
Find the missing element.
"""


# 1. Via Natural Sum n * (n + 1 ) // 2
def find_missing_element(arr):
    last_element = arr[-1]
    print("Last Number in Array is ===> ", last_element)
    total_sum = last_element * (last_element + 1) // 2
    arr_sum = sum(arr)
    missing_element = total_sum - arr_sum
    print("Missing Element in the Array is ====>", missing_element)


array = [1, 2, 3, 4, 5, 7, 8, 9, 10]
find_missing_element(array)
"""
Result :
Last Number in Array is ===>  10
Missing Element in the Array is ====> 6
"""

# 2. Via XOR Approach
def find_missing_element_xor(arr):
    size = len(arr)
    xor1 = arr[0]

    for i in range(1, size):
        xor1 = xor1 ^ arr[i]
    xor2 = 0
    for i in range(1, size + 2):
        xor2 = xor2 ^ i
    print("Missing Element  ===> ", xor1 ^ xor2)


find_missing_element_xor(array)
"""
Result :
Missing Element  ===>  6
"""
