class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        m = len(key)

        def count(curr, next):
            bet = abs(curr - next)
            arr = n - bet
            return min(bet, arr)

        charInd = collections.defaultdict(list)
        for i, char in enumerate(ring):
            charInd[char].append(i)

        heap = [(0, 0, 0)]
        seen = set()
        while heap:
            total, rinfInd, keyInd = heapq.heappop(heap)
            if keyInd == m:
                break

            if (rinfInd, keyInd) in seen:
                continue

            seen.add((rinfInd, keyInd))
            for nextInd in charInd[key[keyInd]]:
                heapq.heappush(
                    heap, (total + count(rinfInd, nextInd), nextInd, keyInd + 1)
                )

        return total + m
