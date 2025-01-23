class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1, m):
            n = len(triangle[i])
            for j in range(n):
                if j == 0:
                    triangle[i][j] += triangle[i - 1][j]
                elif j == n - 1:
                    triangle[i][j] += triangle[i - 1][j - 1]
                else:
                    triangle[i][j] += min(triangle[i - 1][j], triangle[i - 1][j - 1])

        return min(triangle[m - 1])
