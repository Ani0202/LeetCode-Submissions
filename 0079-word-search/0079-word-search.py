class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, index) -> bool:
            if index == len(word) - 1:
                return board[x][y] == word[index]
            if board[x][y] != word[index]:
                return False
            temp = board[x][y]
            board[x][y] = "0"
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dx, dy in directions:
                X, Y = x + dx, y + dy
                if 0 <= X < rows and 0 <= Y < cols and board[X][Y] != "0":
                    if dfs(X, Y, index + 1):
                        return True
            board[x][y] = temp
            return False

        rows, cols = len(board), len(board[0])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        return False
