class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted([[nums2[i], nums1[i]] for i in range(len(nums1))], reverse=True)
        curr = 0
        ans = 0
        heap = []
        for num2, num1 in nums:
            heapq.heappush(heap, num1)
            curr += num1
            if len(heap) == k:
                ans = max(ans, num2 * curr)
                temp = heapq.heappop(heap)
                curr -= temp

        return ans
