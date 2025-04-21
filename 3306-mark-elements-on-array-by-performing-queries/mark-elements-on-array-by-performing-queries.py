import heapq


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        heap = [(num, ind) for ind, num in enumerate(nums)]
        heapq.heapify(heap)
        i = 0
        total = sum(nums)
        marked = set()
        ans = [0 for _ in range(len(queries))]
        while heap and i < len(queries):
            ind, k = queries[i]
            if ind not in marked:
                total -= nums[ind]
                marked.add(ind)
            while heap and k != 0:
                num, j = heapq.heappop(heap)
                if j not in marked:
                    total -= num
                    marked.add(j)
                    k -= 1

            ans[i] = total
            i += 1

        return ans
