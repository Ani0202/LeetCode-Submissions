class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        ans = 0
        i = 0
        rep = False
        for j in range(1, n):
            if s[j] == s[j - 1]:
                if rep:
                    while s[i] != s[i + 1]:
                        i += 1

                    i += 1
                else:
                    rep = True

            ans = max(ans, j - i + 1)

        return ans
