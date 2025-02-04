class Solution:
    def findLatestTime(self, s: str) -> str:
        ans = ""
        if s[0] == "?":
            if s[1] == "?" or s[1] < "2":
                ans += "1"
            else:
                ans += "0"
        else:
            ans += s[0]

        if s[1] == "?":
            if ans[0] == "1":
                ans += "1"
            else:
                ans += "9"
        else:
            ans += s[1]

        ans += ":"
        if s[3] == "?":
            ans += "5"
        else:
            ans += s[3]

        if s[4] == "?":
            ans += "9"
        else:
            ans += s[4]

        return ans
