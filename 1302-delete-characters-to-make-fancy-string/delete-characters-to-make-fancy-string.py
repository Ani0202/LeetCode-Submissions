class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        if n <= 2:
            return s

        ans = s[0:2]
        for i in range(2, len(s)):
            if not (s[i - 2] == s[i - 1] == s[i]):
                ans += s[i]

        return ans
