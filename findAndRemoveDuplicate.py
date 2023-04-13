"""

https://www.geeksforgeeks.org/print-all-the-duplicates-in-the-input-string/

"""
from collections import defaultdict


# Using Map
# Time Complexity: O(nlogn)
# Space complexity: O(k) , k= size of map
def printDuplicate(inputString):
    map = defaultdict(int)
    for x in range(len(inputString)):
        map[inputString[x]] += 1
    for char in map:
        if map[char] > 1:
            print(char, ", count = ", map[char])


str = 'deepppaaakkkkk'
printDuplicate(str)


# Using Stack
# Time Complexity : O(n)
# Space Complexity: O(n)
def removeDuplicate(inputString):
    stack = []
    lastOccurance = {char: x for x, char in enumerate(inputString)}
    print(lastOccurance)
    # {'s': 2, 'i': 5, 'n': 6, 'g': 7, 'h': 8}

    for x, char in enumerate(inputString):
        if char in stack:
            continue
        while stack and char < stack[-1] and x < lastOccurance[stack[-1]]:
            stack.pop()
        stack.append(char)
    print(''.join(stack))
    # singh
    return ''.join(stack)


str = 'sssiiingh'
removeDuplicate(str)
