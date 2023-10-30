"""
Given an array of meeting time intervals consisting of start and end times
 [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

"""
import heapq


# Using Priority Queue : Heap
# Time Complexity: O(sort)
# Space Complexity: O(n)

def meetingRooms(intervals):
    minHeap = [] # store end times of each room
    srt = sorted(intervals)
    for start , end in srt:
        if minHeap and start >= minHeap[0]: # If No Overlap use the same room
            heapq.heappop(minHeap)
        heapq.heappush(minHeap,end)
    return len(minHeap)


interval =  [[0, 30],[5, 10],[15, 20]]
print(" Minimum Number of rooms required", meetingRooms(interval))


# Using Sort + 2 pointers
# Time Complexity: O(sort)
# Space Complexity: O(n)


def meetingRoom2PointerSort(arr):
    n = len(arr)
    starts, ends = [],[] # Empty list
    result = 0
    for start, end in arr:
        starts.append(start)
        ends.append(end)
    starts.sort()
    ends.sort()

    y = 0
    for x in range(n):
        if starts[x] < ends[y]:
            result += 1
        else :
            y += 1
    return result





interval =  [[0, 30],[5, 10],[15, 20]]
print(" Minimum Number of rooms required", meetingRoom2PointerSort(interval))
