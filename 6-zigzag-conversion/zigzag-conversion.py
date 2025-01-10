class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = ["" for _ in range(numRows)]
        dir = -1
        i = 0
        for letter in s:
            ans[i] += letter
            if i == 0 or i == numRows - 1:
                dir *= -1
            i += dir

        return "".join(ans)
