class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "-"

        def markSafe(x, y, board):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != "-":
                return

            board[x][y] = "O"
            markSafe(x, y+1, board)
            markSafe(x-1, y, board)
            markSafe(x, y-1, board)
            markSafe(x+1, y, board)

        for i in range(m):
            if board[i][0] == "-":
                markSafe(i, 0, board)
        
        for i in range(n):
            if board[m-1][i] == "-":
                markSafe(m-1, i, board)
        
        for i in range(m-1, -1, -1):
            if board[i][n-1] == "-":
                markSafe(i, n-1, board)
        
        for i in range(n-1, -1, -1):
            if board[0][i] == "-":
                markSafe(0, i, board)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "-":
                    board[i][j] = "X"

        