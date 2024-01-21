class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0,0]
        for i in range(n):
            temp = [0,0]
            temp[0] = max(dp)
            temp[1] = nums[i] + dp[0]
            dp = temp
        return max(dp)
        