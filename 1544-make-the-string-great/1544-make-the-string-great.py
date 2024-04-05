class Solution:
    def makeGood(self, s: str) -> str:
        ans = ""
        for i in s:
            if len(ans) and abs(ord(ans[-1]) - ord(i)) == 32:
                ans = ans[:-1]
            else:
                ans += i

        return ans
