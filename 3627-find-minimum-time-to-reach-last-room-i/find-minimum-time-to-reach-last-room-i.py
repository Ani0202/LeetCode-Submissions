import heapq


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        dist = [[float("inf") for _ in range(m)] for _ in range(n)]
        dist[0][0] = 0
        heap = []
        heapq.heappush(heap, [0, 0, 0])
        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        while heap:
            d, x, y = heapq.heappop(heap)
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X <= n - 1 and 0 <= Y <= m - 1:
                    if dist[X][Y] > max(dist[x][y], moveTime[X][Y]) + 1:
                        dist[X][Y] = max(dist[x][y], moveTime[X][Y]) + 1
                        heapq.heappush(heap, [dist[X][Y], X, Y])

        return dist[n - 1][m - 1]
