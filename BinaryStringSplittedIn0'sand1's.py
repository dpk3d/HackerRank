"""
https://www.geeksforgeeks.org/split-the-binary-string-into-substrings-with-equal-number-of-0s-and-1s/

"""


# Brute Force Approach
# TIme Complexity : O(N) , Space Complexity : O(1)

def binary_split_string(input_string):
    countZero = 0
    countOne = 0
    count = 0
    for x in range(len(input_string)):
        if input_string[x] == "0":
            countZero += 1
        else:
            countOne += 1
        if countOne == countZero:
            count += 1
    if countOne != countZero:
        return -1
    return count


str = "0000000000"
print("Output is : ", binary_split_string(str))
# Output is :  -1
