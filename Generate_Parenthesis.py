"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""


# Using Backtracking Optimal Approach
def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def backTracking(currPosition, openLeft, closeLeft):
            if openLeft == 0 and closeLeft == 0:
                out.append(currPosition)
            if openLeft > 0:
                backTracking(currPosition + '(', openLeft - 1, closeLeft + 1)
            if closeLeft > 0:
                backTracking(currPosition + ')', openLeft, closeLeft - 1)
        backTracking('', n, 0)
        return out
      
      
### Using Stack

    def generateParenthesis(self, n):
        list = []
        str = '('
        stack = 1
        recursive(list, n, str, 1)
        return list
        

def recursive(list, n, str, stack):

if len(str) == 2*n:
	list.append(str)
	return

if str.count('(') != n and stack >= 0:
	str1 = str + '('
	recursive(list, n, str1, stack + 1)

if str.count(')') != n and stack >= 0:
	str2 = str + ')'
	recursive(list, n, str2, stack - 1)
  
