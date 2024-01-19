class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [0 for _ in range(n+1)]
        for i in range(m):
            tempDp = [0 for _ in range(n+1)]
            for j in range(n):
                if matrix[i][j] == "1":
                    tempDp[j+1] = 1 + min(tempDp[j], dp[j], dp[j+1])
                    ans = max(ans, tempDp[j+1])
            dp = tempDp
        return ans * ans
        