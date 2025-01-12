class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def findParen(oppn, clpn, temp):
            if clpn == n:
                ans.append(temp[:])
                return

            if oppn < n:
                temp += "("
                findParen(oppn + 1, clpn, temp)
                temp = temp[:-1]

            if clpn < oppn:
                temp += ")"
                findParen(oppn, clpn + 1, temp)
                temp = temp[:-1]

        findParen(0, 0, "")
        return ans
