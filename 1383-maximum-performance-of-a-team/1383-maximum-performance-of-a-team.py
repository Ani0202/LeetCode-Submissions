class Solution:
    def maxPerformance(
        self, n: int, speed: List[int], efficiency: List[int], k: int
    ) -> int:
        ans = 0
        totalSpeed = 0
        A = sorted([(e, s) for s, e in zip(speed, efficiency)], reverse=True)
        minHeap = []

        for e, s in A:
            if len(minHeap) == k:
                totalSpeed -= heapq.heappop(minHeap)
            heapq.heappush(minHeap, s)
            totalSpeed += s
            ans = max(ans, totalSpeed * e)

        return ans % 1000000007
