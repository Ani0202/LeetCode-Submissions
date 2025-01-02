import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        A = []
        for i in nums:
            A.append(-i)
        heapq.heapify(A)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(A)

        return -ans