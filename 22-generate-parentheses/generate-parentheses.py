class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        temp = []

        def build_par(temp, o, c):
            if c == 0:
                ans.append("".join(temp))
                return

            if o != 0:
                temp.append("(")
                build_par(temp, o - 1, c)
                temp.pop()
            if c > o:
                temp.append(")")
                build_par(temp, o, c - 1)
                temp.pop()

        build_par(temp, n, n)
        return ans
