"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


# sort method to a list costs O(nlogn), where n is the length of the list.
# The for-loop used to merge intervals, costs O(n). O(nlogn)+O(n) = O(nlogn)
# So the total time complexity is O(nlogn).
# The algorithm used a merged list and a variable i.
# In the worst case, the merged list is equal to the length of the input intervals list.
# So the space complexity is O(n), where n is the length of the input list.
def mergeInterval(intervals):
    result = []
    for interval in sorted(intervals, key=lambda x: x[0]):
        if result and interval[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            result.append(interval)
    return result


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print("merged interval is : ",mergeInterval(intervals))
