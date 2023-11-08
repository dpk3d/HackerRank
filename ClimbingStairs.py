"""

https://leetcode.com/problems/climbing-stairs/description/

https://www.geeksforgeeks.org/count-ways-reach-nth-stair/

"""


# Memoization Concept with recursion
# Time Complexity : O(n)
# Space Complexity : O(n)


def climbStairs(self, n: int) -> int:
    memo = {}  # Storing already computed result for each step
    return self.recursive(n, memo)


def recursive(self, n: int, memo: dict[int, int]) -> int:
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = self.recursive(n - 1, memo) + self.recursive(n - 2, memo)
    return memo[n]


# Dynamic Programming Tabulation bottom up aprroach
# Time Complexity : O(n)
# Space Complexity : O(n)


def climbStairsTabulation(self, n: int) -> int:
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1

    for i in range(2, n + 1):
        # updating DP table by summing up the values for the previous two steps
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Optimal Approach : Using two pointer
# Time Complexity : O(n)
# Space Complexity : O(1)

def climbStairsOptimal(self, n: int) -> int:
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n + 1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


