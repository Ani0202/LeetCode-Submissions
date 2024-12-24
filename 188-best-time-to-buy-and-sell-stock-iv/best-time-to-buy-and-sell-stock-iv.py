class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or k == 0:
            return 0

        profits = [[0] * 2 for _ in range(k + 1)]
        for j in range(1, k + 1):
            profits[j][1] = -prices[0]

        for price in prices[1:]:
            for j in range(k, 0, -1):
                profits[j][0] = max(profits[j][1] + price, profits[j][0])
                profits[j][1] = max(profits[j - 1][0] - price, profits[j][1])

        return profits[k][0]
