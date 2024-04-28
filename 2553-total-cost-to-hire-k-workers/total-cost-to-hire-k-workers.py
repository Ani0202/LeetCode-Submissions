class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        head = costs[:candidates]
        tail = costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(head)
        heapq.heapify(tail)
        ans = 0
        i = candidates
        j = len(costs) - 1 - candidates
        for _ in range(k):
            if not tail or head and head[0] <= tail[0]:
                ans += heapq.heappop(head)
                if i <= j:
                    heapq.heappush(head, costs[i])
                    i += 1
            else:
                ans += heapq.heappop(tail)
                if i <= j:
                    heapq.heappush(tail, costs[j])
                    j -= 1

        return ans
