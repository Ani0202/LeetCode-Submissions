class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        ans = []
        for word in words:
            n = len(word)
            dp = [False for _ in range(n + 1)]
            dp[0] = True
            for i in range(1, n + 1):
                for j in range((i == n) and 1 or 0, i):
                    if not dp[i]:
                        dp[i] = dp[j] and word[j:i] in s
            if dp[n]:
                ans.append(word)

        return ans
