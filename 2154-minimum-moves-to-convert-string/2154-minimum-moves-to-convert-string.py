class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        oSet = set()
        for i in range(n):
            if s[i] == "O":
                oSet.add(i)

        ans = 0
        for i in range(len(s)):
            if i not in oSet:
                ans += 1
                oSet = oSet.union([i, i + 1, i + 2])

        return ans
