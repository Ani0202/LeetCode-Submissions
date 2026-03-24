class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ""
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (
                    i == j
                    or j == i + 1
                    or (i < n - 1 and j > 0 and dp[i + 1][j - 1] == 1)
                ):
                    dp[i][j] = 1
                    if max_len < j - i + 1:
                        max_len = j - i + 1
                        ans = s[i : j + 1]

        return ans
