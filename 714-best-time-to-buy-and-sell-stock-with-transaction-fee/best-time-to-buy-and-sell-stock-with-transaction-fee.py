class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [0, -prices[0]]
        for i in range(1, n):
            dp = [max(dp[0], dp[1] + prices[i] - fee), max(dp[1], dp[0] - prices[i])]

        return max(dp)
