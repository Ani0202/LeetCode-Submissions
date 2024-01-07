class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n] += 1
        heap = [-i for i in hmap.values()]
        heapq.heapify(heap)
        ans = len(nums)
        while len(heap) > 1:
            i = -heapq.heappop(heap)
            j = -heapq.heappop(heap)
            i -= 1
            j -= 1
            ans -= 2
            if i > 0:
                heapq.heappush(heap, -i)
            if j > 0:
                heapq.heappush(heap, -j)

        return ans
        