import heapq


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = 0
        people.sort(reverse=True)
        heap = []
        for weight in people:
            if heap and heap[0] + weight <= limit:
                heapq.heappop(heap)
            else:
                heapq.heappush(heap, weight)
                count += 1

        return count
