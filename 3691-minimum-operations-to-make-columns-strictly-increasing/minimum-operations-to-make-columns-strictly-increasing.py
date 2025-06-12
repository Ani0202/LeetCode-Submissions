class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        prev = grid[0]
        incr = 0
        for i in range(1, m):
            for j in range(n):
                if grid[i][j] <= prev[j]:
                    incr += prev[j] + 1 - grid[i][j]
                    prev[j] += 1
                else:
                    prev[j] = grid[i][j]

        return incr
