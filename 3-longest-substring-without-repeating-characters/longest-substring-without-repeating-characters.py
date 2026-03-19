class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev_inds = dict()
        i = 0
        ans = 0
        for j in range(len(s)):
            if s[j] in prev_inds:
                i = max(prev_inds[s[j]] + 1, i)

            prev_inds[s[j]] = j
            ans = max(ans, j - i + 1)

        return ans
