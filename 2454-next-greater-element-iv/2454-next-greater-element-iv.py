from heapq import heappop, heappush
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        stack = []
        heap = []
        ans = [-1 for i in range(len(nums))]
        for i,n in enumerate(nums):
            while heap and heap[0][0] < n:
                ans[heap[0][1]] = n
                heappop(heap)
            while stack and nums[stack[-1]] < n:
                heappush(heap, [nums[stack[-1]], stack.pop()])
            stack.append(i)

        return ans
        