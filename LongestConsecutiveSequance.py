"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

    0 <= nums.length <= 105
    -109 <= nums[i] <= 109

"""


# Time Complexity is O(NlogN) , Space is O(1)
def bruteForce(arr):
    arr.sort()
    longest, currLongest = 0, min(1, len(arr))
    for x in range(1, len(arr)):
        # array[x] == array[x-1]: same element as previous. Skip it and go to next element in the sequence , if exist .
        if arr[x] == arr[x - 1]:
            continue
        # array[x] == array[x-1] + 1:  current element is consecutive to previous, so increment current streak count.
        elif arr[x] == arr[x - 1] + 1:
            currLongest += 1
        else:
            longest, currLongest = max(longest, currLongest), 1
    return max(longest, currLongest)


arr = [100, 4, 200, 1, 3, 2]
print(" Longest Consecutive Subsequence is : ", bruteForce(arr))


# Time Complexity O(N), Space Complexity O(N)
def longestConsecutive(arr):
    hset = set(arr)
    longest = 0
    for x in hset:
        if x - 1 in hset:
            continue
        a = 0
        while x + a in hset:
            a += 1
        longest = max(longest, a)
    return longest


arr = [100, 4, 200, 1, 3, 2, 6, 6, 5, 5]
print(" Longest Consecutive Subsequence Using Set is : ", longestConsecutive(arr))
