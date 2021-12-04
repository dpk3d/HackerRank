"""
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. 
For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. 
Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

Solution : https://www.geeksforgeeks.org/stock-buy-sell/

"""

"""
Problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
---------
Logic : 
---------
You buy stock by today price and hold, price is hold , if price at next day is less than Today's price, hold is replace.
otherwise , sold stock, but if next day , the profit (profit) is higher , you sold by next profit.

Dynamic Programing
"""
#--------------------------------------------------
def maxProfit(self, prices: List[int]) -> int:
hold , profit = prices[0],0

    for p in prices[1:]:
        if p < hold:            
            hold = p
        else:
            if p-hold >prpfit:
                profit = p-hold
    return profit
# -------------------------------

#------------------------------
def getMaxProfit(arr):
  arrSize = len(arr)
  # Price must be there for minimum 2 days.
  if (arrSize == 1):
    return
  x=0
  while(x < (arrSize - 1)):
    # Getting minimum price and comparing with next element
    while(( x < (arrSize - 1 )) and (arr[x + 1] <= arr[x])):
      x += 1
    if ( x == arrSize - 1):
      break
    buyStock = x
    x += 1
    # Getting Maximum Element
    while ((x < arrSize) and (arr[x] >= arr[x - 1])):
            x += 1
    sellStock = x - 1
    print("Buy on day: ",buyStock,"\t", "Sell on day: ",sellStock)
  #-------------------------------
  
  
  #----------------------
  
      def maxProfit(self, prices: List[int]) -> int:
        run_profit = 0 
        for i in range(len(prices)):
            if i==0:
                buy = prices[i]
            else:
                diff = prices[i] - buy
                
                if diff > 0:
                    run_profit = diff 
                if diff > run_profit else run_profit
                else:
                    buy = prices[i]
        return run_profit
   # -----------------------------------
