class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0 for _ in range(6)] for _ in range(n+1)]
        dp[0][0] = 1
        prevSum = 1
        currSum = 0
        for i in range(1, n+1):
            for j in range(1,6):
                dp[i][j] = prevSum
                prevSum -= dp[i-1][j]
                currSum += dp[i][j]
            prevSum = currSum
            currSum = 0

        return prevSum