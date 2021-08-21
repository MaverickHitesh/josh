# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

def maxProfit(prices: [int]) -> int:
    l, r = 0, 1
    maxP = 0

    while r < len(prices):
        # profitable?
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1
    return maxP
print(maxProfit([7,1,5,3,6,4]))

