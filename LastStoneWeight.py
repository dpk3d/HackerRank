"""
https://leetcode.com/problems/last-stone-weight/

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together.
Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

    If x == y, both stones are destroyed, and
    If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.



Example 1:

Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

Example 2:

Input: stones = [1]
Output: 1



Constraints:

    1 <= stones.length <= 30
    1 <= stones[i] <= 1000


"""
import heapq


def lastStoneWeight(stones):
    negativeStones = [-x for x in stones]
    print(negativeStones)
    # [-2, -7, -4, -1, -8, -1]
    heapq.heapify(negativeStones)
    while len(negativeStones) > 1:
        firstMax = heapq.heappop(negativeStones)
        secondMax = heapq.heappop(negativeStones)
        if secondMax > firstMax:
            heapq.heappush(negativeStones, firstMax - secondMax)
    negativeStones.append(0)
    return abs(negativeStones[0])


stones = [2, 7, 4, 1, 8, 1]
print("The Last weight stone is : ", lastStoneWeight(stones))


def lastStoneWeightAnother(stones):
    negativeStones = [-x for x in stones]
    print(negativeStones)
    # [-2, -7, -4, -1, -8, -1]
    heapq.heapify(negativeStones)
    while len(negativeStones) >= 2:
        difference = heapq.heappop(negativeStones) - heapq.heappop(negativeStones)
        print("Difference is :", difference)
        # Difference is: -1
        # Difference is: -2
        # Difference is: -1
        # Difference is: 0
        if difference != 0:
            heapq.heappush(negativeStones, difference)
    return - negativeStones[0] if len(negativeStones) == 1 else 0


stones = [2, 7, 4, 1, 8, 1]
print("The Last weight stone is : ", lastStoneWeightAnother(stones))
