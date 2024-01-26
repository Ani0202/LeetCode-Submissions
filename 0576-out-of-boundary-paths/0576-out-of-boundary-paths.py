class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        M = 1000000000 + 7
        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        count = 0

        for moves in range(1, maxMove + 1):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == m - 1:
                        count = (count + dp[i][j]) % M
                    else:
                        temp[i][j] += dp[i + 1][j] 
                    if j == n - 1:
                        count = (count + dp[i][j]) % M
                    else:
                        temp[i][j] += dp[i][j + 1]
                    if i == 0:
                        count = (count + dp[i][j]) % M
                    else:
                        temp[i][j] += dp[i - 1][j]
                    if j == 0:
                        count = (count + dp[i][j]) % M
                    else:
                        temp[i][j] += dp[i][j - 1]

            dp = temp

        return count
