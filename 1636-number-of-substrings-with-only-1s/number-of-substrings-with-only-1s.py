class Solution:
    def numSub(self, s: str) -> int:
        mod = 1000000007
        ans = 0
        n = len(s)
        i = 0
        while i < n:
            if s[i] == "1":
                j = i
                while j < n and s[j] == "1":
                    ans = (ans + (j - i + 1)) % mod
                    j += 1

                i = j

            else:
                i += 1

        return ans
