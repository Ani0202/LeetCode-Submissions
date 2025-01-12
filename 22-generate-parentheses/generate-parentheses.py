class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def findParen(oppn, clpn, temp):
            if clpn == n:
                ans.append(temp)
                return

            if oppn < n:
                findParen(oppn + 1, clpn, temp + "(")

            if clpn < oppn:
                findParen(oppn, clpn + 1, temp + ")")

        findParen(0, 0, "")
        return ans
