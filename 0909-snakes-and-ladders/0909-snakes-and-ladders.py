class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def getRowCol(x):
            row, col = (x - 1) // n, (x - 1) % n
            if row % 2 == 1:
                col = n - 1 - col
            return n - 1 - row, col

        n = len(board)
        queue = deque([1])
        visited = {1}
        ans = 0

        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                if x == n * n:
                    return ans
                for y in range(x + 1, min(x + 7, n * n + 1)):
                    i, j = getRowCol(y)
                    if board[i][j] != -1:
                        y = board[i][j]
                    if y not in visited:
                        queue.append(y)
                        visited.add(y)
            ans += 1
        return -1
