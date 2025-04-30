class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minEle = min(nums)
        ans = 0
        for num in nums:
            ans += num - minEle

        return ans
