class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def dfs(x, y):
            board[x][y] = "."
            dx = [0, -1, 0, 1]
            dy = [-1, 0, 1, 0]
            for i in range(4):
                xnew = x + dx[i]
                ynew = y + dy[i]
                if 0 <= xnew < m and 0 <= ynew < n and board[xnew][ynew] == "O":
                    dfs(xnew, ynew)

        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == "O":
                    dfs(i, j)

        for i in range(m):
            for j in (0, n - 1):
                if board[i][j] == "O":
                    dfs(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == ".":
                    board[i][j] = "O"
