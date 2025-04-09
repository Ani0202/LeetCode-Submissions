import heapq


class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        heap = []
        for i in range(n):
            for j in range(m):
                heap.append((-grid[i][j], i))

        heapq.heapify(heap)
        ans = 0
        while k and heap:
            num, row = heapq.heappop(heap)
            if limits[row] > 0:
                limits[row] -= 1
                ans -= num
                k -= 1

        return ans
