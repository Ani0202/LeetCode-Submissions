class Solution:
    def maxOperations(self, s: str) -> int:
        ans = 0
        ones = 0
        for i in range(len(s)):
            if s[i] == "1":
                if i > 0 and s[i - 1] == "0":
                    ans += ones

                ones += 1

        if s[-1] == "0":
            ans += ones

        return ans
