class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        max_consecutive = 1
        for coin in sorted(coins):
            if coin > max_consecutive:
                break
            max_consecutive += coin
        return max_consecutive