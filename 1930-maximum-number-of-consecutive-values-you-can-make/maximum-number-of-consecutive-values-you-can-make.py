class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        ans = 1
        for val in sorted(coins):
            if val > ans:
                break
            ans += val

        return ans
