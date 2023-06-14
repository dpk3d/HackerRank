"""
https://www.geeksforgeeks.org/print-subsequences-string/

"""

# Time Complexity: O(n * 2n), where n is the size of the given string
# Auxiliary Space: O(n), due to recursive call stack
def printSubSequence(inputString, length, index, output):
    if index == length:
        return
    if len(output) > 0:
        print(output)
    x = index + 1
    while x < length:
        output = output + inputString[x]
        printSubSequence(inputString, length, x, output)
        output = output[0: -1]
        x = x + 1


input = "deepak"
n = len(input)
curr = ""
index = -1
print(" Final Output : ", printSubSequence(input, n, index, curr))
# d
# de
# dee
# deep
# deepa
# deepak
# deepk
# deea
# deeak
# deek
# dep
# depa
# depak
# depk
# dea
# deak
# dek
# de
# dep
# depa
# depak
# depk
# dea
# deak
# dek
# dp
# dpa
# dpak
# dpk
# da
# dak
# dk
# e
# ee
# eep
# eepa
# eepak
# eepk
# eea
# eeak
# eek
# ep
# epa
# epak
# epk
# ea
# eak
# ek
# e
#  ep
#  epa
#  epak
# epk
# ea
# eak
# ek
# p
# pa
# pak
# pk
# a
# ak
# k