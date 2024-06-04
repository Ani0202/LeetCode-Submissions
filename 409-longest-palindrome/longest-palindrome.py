class Solution:
    def longestPalindrome(self, s: str) -> int:
        hSet = set()
        ans = 0
        for c in s:
            if c in hSet:
                hSet.remove(c)
                ans += 2
            else:
                hSet.add(c)

        if hSet:
            ans += 1

        return ans
