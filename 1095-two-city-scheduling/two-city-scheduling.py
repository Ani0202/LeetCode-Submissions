class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        heap = []
        ans = 0
        for a, b in costs:
            heapq.heappush(heap, [a - b, a, b])

        for i in range(n // 2):
            c, a, b = heapq.heappop(heap)
            ans += a

        for c, a, b in heap:
            ans += b

        return ans
