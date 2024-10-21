class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        low = 0
        ans = -float("inf")
        curr = 0
        for num in nums:
            curr += num
            ans = max(ans, curr - low)
            low = min(low, curr)

        return ans