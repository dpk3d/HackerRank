"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
"""


def maximum_sum_sub_array(arr):
    size = len(arr)
    current_sum = 0
    maximum_sum_so_far = arr[0]
    start_index = 0
    end_index = 0
    pointer = 0
    for x in range(0, size):
        current_sum = current_sum + arr[x]
        if maximum_sum_so_far < current_sum:
            start_index = pointer
            end_index = x
            maximum_sum_so_far = current_sum
            print("Maximum Sum", maximum_sum_so_far)
        if current_sum < 0:
            current_sum = 0
            pointer = x + 1

    print(" Maximum Sum Sub array is ===> ", maximum_sum_so_far)
    print(" Start index of Maximum Sum Sub array is ===> ", start_index)
    print(" End index of Maximum Sum Sub array is ===> ", end_index)


array = [3, 4, -5, 3, -4, -4, 8, 3, -2, 7, -10]
maximum_sum_sub_array(array)
"""
Result : 
 Maximum Sum Sub array is ===>  16
 Start index of Maximum Sum Sub array is ===>  6
 End index of Maximum Sum Sub array is ===>  9
"""
