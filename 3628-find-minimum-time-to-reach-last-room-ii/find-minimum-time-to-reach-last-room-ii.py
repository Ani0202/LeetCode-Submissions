import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        heap = []
        heapq.heappush(heap, (0, 0, 0, 1))
        while heap:
            d, x, y, t = heapq.heappop(heap)
            for dx, dy in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                X = x + dx
                Y = y + dy
                if 0 <= X <= n - 1 and 0 <= Y <= m - 1:
                    if dist[X][Y] > max(dist[x][y], moveTime[X][Y]) + t:
                        dist[X][Y] = max(dist[x][y], moveTime[X][Y]) + t
                        heapq.heappush(heap, (dist[X][Y], X, Y, (t % 2) + 1))

        return dist[n - 1][m - 1]
