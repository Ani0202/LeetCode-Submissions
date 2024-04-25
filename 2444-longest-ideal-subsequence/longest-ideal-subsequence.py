class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        ans = 0
        for i in range(n):
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(26):
                if abs(prev - curr) <= k:
                    best = max(best, dp[prev])

            dp[curr] = max(dp[curr], best + 1)
            ans = max(ans, dp[curr])

        return ans
        