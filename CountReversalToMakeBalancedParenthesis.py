"""

https://practice.geeksforgeeks.org/problems/count-the-reversals0401/1

Count the Reversals
Given a string S consisting of only opening and closing curly brackets '{' and '}',
find out the minimum number of reversals required to convert the string into a balanced expression.
A reversal means changing '{' to '}' or vice-versa.


Input:
S = "}{{}}{{{"
Output: 3
Explanation: One way to balance is:
"{{{}}{}}". There is no balanced sequence
that can be formed in lesser reversals.

Example 2:

Input:
S = "{{}{{{}{{}}{{"
Output: -1
Explanation: There's no way we can balance
this sequence of braces.



"""


# Time Complexity : O(n)
# Space Complexity : O(1)
# Using Stack
def traversal_count(str):
    stack = []
    result = 0
    for x in str:
        if x == "{":
            stack.append("{")
        elif len(stack) == 0:
            result += 1
            stack.append("{")
        else:
            stack.pop()
    if len(stack) % 2 != 0:
        return -1
    return result + len(stack) // 2


input_string = "{{}{{{}{{}}{{"
input_string1 = "}{{}}{{{"
print(" Minimum number of reversal : ", traversal_count(input_string))
# Minimum number of reversal :  -1
print(" Minimum number of reversal : ", traversal_count(input_string1))
# Minimum number of reversal :  3
