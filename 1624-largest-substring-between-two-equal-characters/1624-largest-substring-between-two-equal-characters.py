class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hmap = dict()
        n = len(s)
        for i in range(n):
            if s[i] not in hmap:
                hmap[s[i]] = i
        ans = -1
        for i in range(n-1, -1, -1):
            if hmap[s[i]] != i:
                ans = max(ans, i - hmap[s[i]] - 1)

        return ans
        