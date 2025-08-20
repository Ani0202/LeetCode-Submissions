class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    ans += matrix[i][j]
                else:
                    if matrix[i][j] == 1:
                        matrix[i][j] = (
                            min(
                                matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]
                            )
                            + 1
                        )
                        ans += matrix[i][j]

        return ans
