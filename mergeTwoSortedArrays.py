"""
Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order.
Merge them in sorted order without using any extra space.
Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.
"""


# This Method has Time complexity of n * n, Space complexity of  O(n)
def mergeTwoSortedArray(arr1, arr2):
    i = 0
    j = 0
    l1 = len(arr1)
    l2 = len(arr2)
    emptyArr = []
    while (i < l1) and (j < l2):
        if arr1[i] < arr2[j]:
            emptyArr.append(arr1[i])
            i = i + 1
        else:
            emptyArr.append(arr2[j])
            j = j + 1
    while i < l1:
        emptyArr.append(arr1[i])
        i = i + 1
    while j < l2:
        emptyArr.append(arr2[j])
        j = j + 1
    print("Final Merged Array", emptyArr)


array1 = [1, 3, 5, 7, 9]
array2 = [2, 4, 8, 10, 12]
mergeTwoSortedArray(array1, array2)

"""
Output :
Final Merged Array [1, 2, 3, 4, 5, 7, 8, 9, 10, 12]
"""


# This solution is Good but not optimal
def mergeTwoSortedArrayInsertion(deepak, moni):
    size_one = len(deepak)
    size_two = len(moni)
    for i in range(size_one):
        # Comparing the current element of deepak with first element of moni
        if deepak[i] > moni[0]:
            # Swapping the element deepak[i] with moni[0]
            temp = deepak[i]
            deepak[i] = moni[0]
            moni[0] = temp
            first_element = moni[0]
            j = 1
            while j < size_two and moni[j] < first_element:
                moni[j - 1] = moni[j]
                j = j + 1
                moni[j - 1] = first_element
    print("First Array", deepak)
    print("Second Array", moni)
    print("Merged Array Via Insertion sort", deepak + moni)


deepak = [1, 3, 5, 7, 9]
moni = [2, 4, 6]

mergeTwoSortedArrayInsertion(deepak, moni)
"""
Output :
First Array [1, 2, 3, 4, 5]
second Array [6, 7, 9]
Merged Array Via Insertion sort [1, 2, 3, 4, 5, 6, 7, 9]
"""


# Here Goes the Best Optimal Solution
# Time Complexity of O(m + n ), Space Complexity O(1)
# Using GAP Algorithm / SHELL SHORT


def calculateGap(length):
    if length <= 1:
        return 0
    return length // 2 + length % 2


def mergeTwoSortedArrayOptimal(deep, moni, deep_length, moni_length):
    totalElement = deep_length + moni_length
    gap = calculateGap(totalElement)
    while gap > 0:
        x = 0
        while x + gap < deep_length:
            if deep[x] > deep[x + gap]:
                deep[x], deep[x + gap] = deep[x + gap], deep[x]
            x += 1
        y = gap - deep_length if gap > deep_length else 0
        while x < deep_length and y < moni_length:
            if deep[x] > moni[y]:
                deep[x], moni[y] = moni[y], deep[x]
            y += 1
            x += 1
        if y < moni_length:
            y = 0
            while y + gap < moni_length:
                if moni[y] > moni[y + gap]:
                    moni[y], moni[y + gap] = moni[y + gap], moni[y]
                y += 1
        gap = calculateGap(totalElement)

    print(" array", deep)


deepakkk = [1, 3, 5, 7, 9, 11, 13, 15, 17]
moniee = [2, 4, 6, 8]
mergeTwoSortedArrayOptimal(deepakkk, moniee, len(deepakkk), len(moniee))
#https://www.geeksforgeeks.org/efficiently-merging-two-sorted-arrays-with-o1-extra-space/
