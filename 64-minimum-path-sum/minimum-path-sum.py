class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[grid[i][j] for j in range(n)] for i in range(m)]
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]

        for i in range(1, n):
            dp[0][i] += dp[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])

        return dp[m - 1][n - 1]
