class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        def dfs(x, y):
            if (
                x < 0
                or x >= len(grid)
                or y < 0
                or y >= len(grid[0])
                or grid[x][y] == "0"
            ):
                return
            grid[x][y] = "0"
            dx = [0, -1, 0, 1]
            dy = [-1, 0, 1, 0]
            for i in range(4):
                dfs(x + dx[i], y + dy[i])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans
