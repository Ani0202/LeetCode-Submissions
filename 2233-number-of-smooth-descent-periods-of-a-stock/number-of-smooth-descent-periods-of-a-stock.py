class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 1
        i = 0
        j = 1
        while j < n:
            if prices[j - 1] - prices[j] != 1:
                i = j

            ans += j - i + 1
            j += 1

        return ans
