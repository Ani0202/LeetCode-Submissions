class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total % 2 != 0:
            return False

        dp = [[False for _ in range(n + 1)] for _ in range((total // 2) + 1)]
        for i in range(n + 1):
            dp[0][i] = True

        for i in range(1, (total // 2) + 1):
            for j in range(1, n + 1):
                if nums[j - 1] <= i:
                    dp[i][j] = dp[i][j - 1] or dp[i - nums[j - 1]][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[total // 2][n]
