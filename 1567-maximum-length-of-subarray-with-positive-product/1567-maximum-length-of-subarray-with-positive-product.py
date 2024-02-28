class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        neg = 0
        pos = 0

        for num in nums:
            pos = 0 if num == 0 else pos + 1
            neg = 0 if num == 0 or neg == 0 else neg + 1
            if num < 0:
                pos, neg = neg, pos
            ans = max(ans, pos)

        return ans
