class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minPrice = prices[0]
        for price in prices[1:]:
            profit = max(profit, price - minPrice)
            minPrice = min(minPrice, price)

        return profit
