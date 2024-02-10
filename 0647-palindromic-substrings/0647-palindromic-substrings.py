class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                    ans += 1
                elif s[i] == s[j]:
                    if j == i + 1:
                        dp[i][j] = 2
                        ans += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = 2 + dp[i + 1][j - 1]
                        ans += 1
        return ans
