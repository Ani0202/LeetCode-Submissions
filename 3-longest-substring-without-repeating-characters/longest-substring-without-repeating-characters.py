class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        prev_strs = set()
        i = 0
        ans = 0
        for j in range(n):
            curr_str = s[j]
            if curr_str in prev_strs:
                while i <= j:
                    prev_strs.remove(s[i])
                    if s[i] == s[j]:
                        i += 1
                        break

                    i += 1

            prev_strs.add(s[j])
            ans = max(ans, j - i + 1)

        return ans
