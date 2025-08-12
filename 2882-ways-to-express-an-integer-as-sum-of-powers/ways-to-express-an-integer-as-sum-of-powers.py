class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 1000000007
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            j = i**x
            for k in range(n, j - 1, -1):
                dp[k] = (dp[k] + dp[k - j]) % MOD

        return dp[n] % MOD
