class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row, cols, diag, anti_diag):
            nonlocal count
            if row == n:
                count += 1
                return
            for col in range(n):
                if col not in cols and row + col not in diag and row - col not in anti_diag:
                    backtrack(row + 1, cols | {col}, diag | {row + col}, anti_diag | {row - col})

        count = 0
        backtrack(0, set(), set(), set())
        return count