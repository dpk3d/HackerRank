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
