import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        heap = [[capital[i], profits[i]] for i in range(n)]
        profitsArr = []
        heapq.heapify(heap)
        ans = 0
        while k:
            while heap and heap[0][0] <= w:
                cap, prof = heapq.heappop(heap)
                heapq.heappush(profitsArr, -prof)

            if len(profitsArr) == 0:
                break

            w -= heapq.heappop(profitsArr)
            k -= 1

        return w
