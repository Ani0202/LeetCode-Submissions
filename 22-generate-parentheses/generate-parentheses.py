class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []

        def build_par(temp, o, c):
            if c == 0:
                self.ans.append(temp)
                return

            if o != 0:
                build_par(temp + "(", o - 1, c)
            if c > o:
                build_par(temp + ")", o, c - 1)

        build_par("", n, n)
        return self.ans
