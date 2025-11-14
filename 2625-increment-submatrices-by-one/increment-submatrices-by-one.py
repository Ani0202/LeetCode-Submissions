class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n + 1) for _ in range(n + 1)]
        for row1, col1, row2, col2 in queries:
            diff[row1][col1] += 1
            diff[row1][col2 + 1] -= 1
            diff[row2 + 1][col1] -= 1
            diff[row2 + 1][col2 + 1] += 1

        mat = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                sum_above = diff[r - 1][c] if r > 0 else 0
                sum_left = diff[r][c - 1] if c > 0 else 0
                sum_diag = diff[r - 1][c - 1] if r > 0 and c > 0 else 0
                diff[r][c] = diff[r][c] + sum_above + sum_left - sum_diag
                mat[r][c] = diff[r][c]

        return mat
