class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        firstBuy = -prices[0]
        firstSell = 0
        secondBuy = -prices[0]
        secondSell = 0
        for price in prices[1:]:
            firstBuy = max(firstBuy, -price)
            firstSell = max(firstSell, firstBuy + price)
            secondBuy = max(secondBuy, firstSell - price)
            secondSell = max(secondSell, secondBuy + price)

        return secondSell
