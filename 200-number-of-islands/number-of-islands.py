class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        ans = 0

        def dfs(i, j):
            visited[i][j] = 1
            if i > 0 and visited[i - 1][j] == 0 and grid[i - 1][j] == "1":
                dfs(i - 1, j)
            if j < n - 1 and visited[i][j + 1] == 0 and grid[i][j + 1] == "1":
                dfs(i, j + 1)
            if i < m - 1 and visited[i + 1][j] == 0 and grid[i + 1][j] == "1":
                dfs(i + 1, j)
            if j > 0 and visited[i][j - 1] == 0 and grid[i][j - 1] == "1":
                dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 0 and grid[i][j] == "1":
                    ans += 1
                    dfs(i, j)

        return ans
