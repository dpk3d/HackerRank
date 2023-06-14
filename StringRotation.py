"""
https://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other/

Given a string s1 and a string s2, write a function to check whether s2 is a rotation of s1.

Examples:

    Input: S1 = ABCD, S2 = CDAB
    Output: Strings are rotations of each other

    Input: S1 = ABCD, S2 = ACBD
    Output: Strings are not rotations of each other

"""


# Using Queue

def checkRotation(inputString1, inputString2):
    if len(inputString1) != len(inputString2):
        print('not possible')
    queue1 = []
    queue2 = []
    for x in range(len(inputString1)):
        queue1.insert(0, inputString1[x])

    for y in range(len(inputString2)):
        queue2.insert(0, inputString2[y])

    N = len(inputString1)
    while N > 0:
        char = queue1[0]
        queue1.pop(0)
        queue1.append(char)
        if queue1 == queue2:
            print(' String is rotation of each other')
            return True
        N -= 1
    print(" Strings are not Rotation of each other")
    return False


string1 = "AACD"
string2 = "ACDA"
checkRotation(string1, string2)
# String is rotation of each other
