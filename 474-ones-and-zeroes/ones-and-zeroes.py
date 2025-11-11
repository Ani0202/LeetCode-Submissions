class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        num_strs = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(num_strs + 1)]
        for i, curr in enumerate(strs, 1):
            zeros = curr.count("0")
            ones = curr.count("1")
            for zeros_limit in range(m + 1):
                for ones_limit in range(n + 1):
                    dp[i][zeros_limit][ones_limit] = dp[i - 1][zeros_limit][ones_limit]
                    if zeros_limit >= zeros and ones_limit >= ones:
                        dp[i][zeros_limit][ones_limit] = max(
                            dp[i][zeros_limit][ones_limit],
                            dp[i - 1][zeros_limit - zeros][ones_limit - ones] + 1,
                        )

        return dp[num_strs][m][n]
