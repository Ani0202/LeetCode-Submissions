class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladds = []
        n = len(heights)
        for i in range(n - 1):
            diff = heights[i + 1] - heights[i]
            if diff > 0:
                heapq.heappush(ladds, diff)
                if len(ladds) > ladders:
                    bUsed = heapq.heappop(ladds)
                    bricks -= bUsed
                    if bricks < 0:
                        return i

        return n - 1
