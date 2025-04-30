import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        ele = -1
        for _ in range(n):
            ele = heapq.heappop(heap)
            while heap and ele == heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap, ele * 2)
            heapq.heappush(heap, ele * 3)
            heapq.heappush(heap, ele * 5)

        return ele
