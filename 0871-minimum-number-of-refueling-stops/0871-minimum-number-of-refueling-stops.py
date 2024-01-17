from heapq import heappop, heappush
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        prev = 0
        heap = []
        ans = 0
        stations.append([target, 0])
        for p,f in stations:
            used = p-prev
            startFuel -= used
            while startFuel < 0 and heap:
                ref = heappop(heap)
                startFuel -= ref
                ans += 1
            if startFuel < 0:
                return -1
            heappush(heap, -f)
            prev = p
        return ans
        