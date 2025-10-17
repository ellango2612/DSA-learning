'''
Best Time to Buy and Sell Stock
 
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100

1:45pm
'''

## use sliding window technique: have l = 0 and r = 1. slide if find a smaller left, but r+=1 at every loop. make l = r when saw a new min for buy day

def maxProfit(self, prices):#prices = [10,1,5,6,7,1], l = 1, r = 2, max_profit = 6
    max_profit = 0
    l, r = 0, 1
    while r < len(prices):
        if prices[r] > prices[l]: #if foudn a profit
            max_profit = max(max_profit, prices[r]-prices[l])
        else:
            l = r
        r+=1
    return max_profit

# Time: O(n)
# Space: O(1)