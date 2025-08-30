class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 10 for _ in range(10)]
        cols = [[0] * 10 for _ in range(10)]
        subBoard = [[0] * 10 for _ in range(10)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                val = int(board[i][j])
                if rows[i][val] == 1:
                    return False

                rows[i][val] = 1
                if cols[j][val] == 1:
                    return False

                cols[j][val] = 1
                idx = (i // 3) * 3 + j // 3
                if subBoard[idx][val] == 1:
                    return False

                subBoard[idx][val] = 1

        return True
