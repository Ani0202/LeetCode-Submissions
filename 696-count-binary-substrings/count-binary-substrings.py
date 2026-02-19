class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev = 0
        curr = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1

            if curr <= prev:
                ans += 1

        return ans
