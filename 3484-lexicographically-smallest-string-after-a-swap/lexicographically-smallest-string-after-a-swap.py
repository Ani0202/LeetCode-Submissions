class Solution:
    def getSmallestString(self, s: str) -> str:
        n = len(s)
        for i in range(n - 1):
            a = int(s[i])
            b = int(s[i + 1])
            if (a ^ b) & 1 == 0 and a > b:
                return s[:i] + s[i + 1] + s[i] + s[i + 2 :]

        return s
