class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        captures = 0
        directions = (-1, 0), (0, 1), (1, 0), (0, -1)
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    for d in directions:
                        x, y = i, j
                        while 0 <= x + d[0] < 8 and 0 <= y + d[1] < 8:
                            x += d[0]
                            y += d[1]
                            if board[x][y] == "p":
                                captures += 1
                                break
                            if board[x][y] != ".":
                                break
        return captures
