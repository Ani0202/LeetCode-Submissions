class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            grid[i].sort()

        ans = 0
        for i in range(n):
            ans += max(grid[j][i] for j in range(m))

        return ans
