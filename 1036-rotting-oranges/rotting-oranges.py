class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
      
        ans = 0
        while queue and fresh > 0:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        fresh -= 1
                        grid[x][y] = 2
                        queue.append((x, y))
      
        return ans if fresh == 0 else -1