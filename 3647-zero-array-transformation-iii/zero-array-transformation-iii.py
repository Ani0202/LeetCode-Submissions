import heapq


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        queries.sort(key=lambda x: x[0])
        curr = 0
        newArr = [0] * (n + 1)
        heap = []
        j = 0
        for i in range(n):
            curr += newArr[i]
            while j < m and queries[j][0] == i:
                heapq.heappush(heap, -queries[j][1])
                j += 1

            while curr < nums[i] and heap and -heap[0] >= i:
                newArr[-heappop(heap) + 1] -= 1
                curr += 1

            if curr < nums[i]:
                return -1

        return len(heap)
