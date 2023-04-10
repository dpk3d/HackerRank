"""
https://practice.geeksforgeeks.org/problems/find-the-median0527/1

Given an array arr[] of N integers, calculate the median


Example 1:

Input: N = 5
arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array
middle element is the median

Example 2:

Input: N = 4
arr[] = 56 67 30 79
Output: 61
Explanation: In case of even number of
elements, average of two middle elements
is the median.



Your Task:
You don't need to read or print anything. Your task is to complete the function find_median() which takes the array as input parameter and returns the floor value of the median.


Expected Time Complexity: O(n * log(n))
Expected Space Complexity: O(1)


Constraints:
1 <= Length of Array <= 100
1 <= Elements of Array <= 100


"""
import math
from typing import List


# Time: O(NLogN) and Space: O(1)
def medianUnsortedArrayBrute(nums1, nums2):
    nums1 = nums1 + nums2
    nums1 = sorted(nums1)
    n = len(nums1)
    if n % 2 == 0:
        return (nums1[n // 2 - 1] + nums1[(n // 2)]) / 2
    else:
        n = math.ceil(n / 2)
        return nums1[n - 1]


# Driver code
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]

print("Median of unsorted Array : ", medianUnsortedArrayBrute(arr1, arr2))


# Time Complexity: O(logn)
# Auxiliary Space: O(logn)
# Both Array of Equal length
def getMedian(arr1, arr2, n):
    # there is no element in any array
    if n == 0:
        return -1

    # 1 element in each => median of sorted arr made of two arrays will be sum of both elements by 2
    elif n == 1:
        return (arr1[0] + arr2[0]) / 2
    elif n == 2:
        # which implies median = (max(arr1[0], arr2[0])+min(arr1[1],arr2[1]))/2
        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2

    else:
        # calculating medians
        m1 = median(arr1, n)
        m2 = median(arr2, n)

        # then the elements at median position must be between the
        # greater median and the first element of respective array and
        # between the other median and the last element in its respective array.
        if m1 > m2:

            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return getMedian(arr1[:int(n / 2) + 1],
                                 arr2[int(n / 2):], int(n / 2) + 1)

        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n / 2 - 1):],
                                 arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return getMedian(arr1[int(n / 2):],
                                 arr2[0:int(n / 2) + 1], int(n / 2) + 1)


# function to find median of array
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n / 2)]


# Driver code
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
n = len(arr1)
print(int(getMedian(arr1, arr2, n)))


#  O(log (m+n))
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    len1 = len(nums1)
    len2 = len(nums2)
    # when total length is odd, the median is the middle
    if (len1 + len2) % 2 != 0:
        return self.get_kthElement(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
    else:
        # when total length is even, the median is the average of the middle 2
        middle1 = self.get_kthElement(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2)
        middle2 = self.get_kthElement(nums1, nums2, 0, len1 - 1, 0, len2 - 1, (len1 + len2) // 2 - 1)
        return (middle1 + middle2) / 2


def get_kthElement(self, nums1, nums2, start1, end1, start2, end2, k):
    if start1 > end1:
        return nums2[k - start1]
    if start2 > end2:
        return nums1[k - start2]

    middle1 = (start1 + end1) // 2
    middle2 = (start2 + end2) // 2
    middle1_value = nums1[middle1]
    middle2_value = nums2[middle2]

    # if sum of two median's indicies is smaller than k
    if (middle1 + middle2) < k:
        # if nums1 median value bigger than nums2, then nums2's first half will always be positioned before nums1's median, so k would never be in num2's first half
        if middle1_value > middle2_value:
            return self.get_kthElement(nums1, nums2, start1, end1, middle2 + 1, end2, k)
        else:
            return self.get_kthElement(nums1, nums2, middle1 + 1, end1, start2, end2, k)
    # if sum of two median's indicies is bigger than k
    else:
        # if nums1 median value bigger than nums2, then nums2's first half would be merged before nums1's first half, thus k always come before nums1's median, then nums1's second half would never include k
        if middle1_value > middle2_value:
            return self.get_kthElement(nums1, nums2, start1, middle1 - 1, start2, end2, k)
        else:
            return self.get_kthElement(nums1, nums2, start1, end1, start2, middle2 - 1, k)



