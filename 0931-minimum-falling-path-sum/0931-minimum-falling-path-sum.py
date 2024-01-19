class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        dp = [0 for _ in range(n)]
        for i in range(n):
            tempDp = [0 for _ in range(n)]
            for j in range(n):
                if j == 0:
                    tempDp[j] = matrix[i][j] + min(dp[j], dp[j+1])
                elif j == n-1:
                    tempDp[j] = matrix[i][j] + min(dp[j], dp[j-1])
                else:
                    tempDp[j] = matrix[i][j] + min(dp[j-1], dp[j], dp[j+1])
            dp = tempDp
            print(dp)
        return min(dp)
        

        