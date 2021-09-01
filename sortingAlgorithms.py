"""
Sort A Given List/Array.

data_list = [-5, -23, 5, 0, 23, -6, 23, 67]

"""

data_list = [-5, -23, 5, 0, 23, -6, 23, 2, 67]

# Using 2 for loops to sort list not recommended solution
# Complexity of this approach is n * n
for x in range(0, len(data_list)):
    for y in range(x + 1, len(data_list)):
        if data_list[x] > data_list[y]:
            data_list[x], data_list[y] = data_list[y], data_list[x]
print("For Loop : Sorted List is ==>", data_list)
"""
For Loop : Sorted List is ==> [-23, -6, -5, 0, 2, 5, 23, 23, 67]
"""

# While Loop Another Approach better than using two for loops.
# We needed a extra auxiliary space over here called new_list.

new_list = []
while data_list:
    lowest = data_list[0]
    for x in data_list:
        if x < lowest:
            lowest = x
    new_list.append(lowest)
    data_list.remove(lowest)
print(" While Loop : Sorted List is ==> ", new_list)
"""
For Loop : Sorted List is ==> [-23, -6, -5, 0, 2, 5, 23, 23, 67]
"""


# Merge Sort . Steps
# Check List has element more than 1
# Get middle element
# Divide the list in two part based on middle element
# sort the left and right list
# Apply the condition to traverse through all the elements in both the list


def mergeSort(list):
    if len(list) > 1:
        middleElement = len(list) // 2
        left_list = list[:middleElement]
        right_list = list[middleElement:]
        mergeSort(left_list)
        mergeSort(right_list)
        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i + 1
                k = k + 1
            else:
                list[k] = right_list[j]
                j = j + 1
                k = k + 1
        while i < len(left_list):
            list[k] = left_list[i]
            i = i + 1
            k = k + 1
        while j < len(right_list):
            list[k] = right_list[j]
            j = j + 1
            k = k + 1


data_list = [-5, -23, 5, 0, 23, -6, 23, 2, 67]
mergeSort(data_list)
print("Merge Sort  : Sorted List ===>", data_list)
"""
Merge Sort  : Sorted List ===> [-23, -6, -5, 0, 2, 5, 23, 23, 67]

The time complexity of MergeSort is O(n*Log n) in all the 3 cases (worst, average and best) 
as the mergesort always divides the array into two halves 
and takes linear time to merge two halves
"""


# Implementing Quick Sort . Steps are
# Take Pivot Element
# Get Correct Position of Pivot element in the list by rearranging
# Divide List Based on Pivot
# Sort The Sub List Recursively


def pivot_element(input_list, first, last):
    pivot = input_list[first]
    left = first + 1
    right = last
    while True:
        while left <= right and input_list[left] <= pivot:
            left = left + 1
        while left <= right and input_list[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            input_list[left], input_list[right] = input_list[right], input_list[left]
    input_list[first], input_list[right] = input_list[right], input_list[first]
    return right


def quickSort(input_list, first, last):
    if first < last:
        p = pivot_element(input_list, first, last)
        quickSort(input_list, first, p - 1)
        quickSort(input_list, p + 1, last)


# Main
input_list = [-5, -23, 5, 0, 23, -6, 23, 2, 67]
start = 0
end = len(input_list) - 1
quickSort(input_list, start, end)
print("Quick Sort : Sorted List is ===>", input_list)
"""
Quick Sort : Sorted List is ===> [-23, -6, -5, 0, 2, 5, 23, 23, 67]
"""


# Randomized Quick Sort
# Randomized quicksort has expected time complexity as O(nLogn), but worst case time complexity remains same n * n

import random
def random_pivot_element(input_list, first, last):
    random_index = random.randint(first,last)
    input_list[random_index],input_list[last] = input_list[last], input_list[random_index]
    pivot = input_list[last]
    left = first
    right = last - 1
    while True:
        while left <= right and input_list[left] <= pivot:
            left = left + 1
        while left <= right and input_list[right] >= pivot:
            right = right - 1
        if right < left:
            break
        else:
            input_list[left], input_list[right] = input_list[right], input_list[left]
    input_list[last], input_list[left] = input_list[left], input_list[last]
    return left


def randomQuickSort(input_list, first, last):
    if first < last:
        p = random_pivot_element(input_list, first, last)
        randomQuickSort(input_list, first, p - 1)
        randomQuickSort(input_list, p + 1, last)


# Main
input_list = [-5, -23, 5, 0, 23, -6, 23, 2, 67, 28]
start = 0
end = len(input_list) - 1
randomQuickSort(input_list, start, end)
print("Randomised Quick Sort : Sorted List is ===>", input_list)
"""
Randomised Quick Sort : Sorted List is ===> [-23, -6, -5, 0, 2, 5, 23, 23, 28, 67]
"""

