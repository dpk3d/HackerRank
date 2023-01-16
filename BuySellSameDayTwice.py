"""
In daily share trading, a buyer buys shares in the morning and sells them on the same day. If the trader is
allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is
complete (Buy->sell->Buy->sell). Given stock priceArray throughout the day, find out the maximum profit that a share
trader could have made.

Examples:

Input:   price[] = {10, 22, 5, 75, 65, 80}
Output:  87
Trader earns 87 as sum of 12, 75
Buy at 10, sell at 22,
Buy at 5 and sell at 80
Input:   price[] = {2, 30, 15, 10, 8, 25, 80}
Output:  100
Trader earns 100 as sum of 28 and 72
Buy at price 2, sell at 30, buy at 8 and sell at 80
Input:   price[] = {100, 30, 15, 10, 8, 25, 80};
Output:  72
Buy at price 8 and sell at 80.
Input:   price[] = {90, 80, 70, 60, 50}
Output:  0
Not possible to earn.

"""


# Time Complexity :- O(N)
def maxProfitDPway(arr):
    length = len(arr)
    maxPrice = arr[length - 1]  # till here only one transaction
    minPrice = arr[0]
    maxProfit = [0] * length
    for x in range(length - 2, 0, -1):
        if arr[x] > maxPrice:
            maxPrice = arr[x]
        maxProfit[x] = max(maxProfit[x + 1], maxPrice - arr[x])
    for x in range(1, length):
        if arr[x] < minPrice:
            minPrice = arr[x]
        maxProfit[x] = max(maxProfit[x - 1], maxProfit[x] + (arr[x] - minPrice))
    return maxProfit[length - 1]


arr = [10, 22, 5, 75, 65, 80]
print("Maximum Profit : ", maxProfitDPway(arr))


def maxProfit(priceArray):
    if not priceArray or len(priceArray) == 1:
        return 0
    profit = 0
    for x in range(1, len(priceArray)):
        if priceArray[x] > priceArray[x - 1]:
            profit += priceArray[x] - priceArray[x - 1]

    return profit


arr = [100, 30, 15, 10, 8, 25, 80]
print("Maximum Profit : ", maxProfit(arr))


def maxProfitShort(arr):
    if len(arr) == 1:  # edge case
        return 0

    # take down positive daily return only
    maxProfit = []
    for x in range(1, len(arr)):
         maxProfit.append(max(0, arr[x] - arr[x - 1]))
    return sum(maxProfit)
