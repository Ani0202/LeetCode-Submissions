class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        def dfs(value, length):
            result = dp[-1][length - 1]
            if length < n:
                multiple = 2
                while multiple * value <= maxValue:
                    result = (result + dfs(multiple * value, length + 1)) % mod
                    multiple += 1
            return result

        dp = [[0] * 16 for _ in range(n)]
        mod = 10**9 + 7
        for i in range(n):
            for j in range(min(16, i + 1)):
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % mod

        answer = 0
        for i in range(1, maxValue + 1):
            answer = (answer + dfs(i, 1)) % mod

        return answer
