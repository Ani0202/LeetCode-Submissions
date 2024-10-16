class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        capitalHeap = [[capital[i], profits[i]] for i in range(n)]
        profitsHeap = []
        heapq.heapify(capitalHeap)
        while k:
            while capitalHeap and capitalHeap[0][0] <= w:
                heapq.heappush(profitsHeap, -heapq.heappop(capitalHeap)[1])

            if len(profitsHeap) == 0:
                break

            w -= heapq.heappop(profitsHeap)
            k -= 1

        return w
