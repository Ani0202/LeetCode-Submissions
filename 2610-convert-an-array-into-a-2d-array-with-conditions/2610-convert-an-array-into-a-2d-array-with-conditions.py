class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        rows = 0
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
            rows = max(rows, hmap[i])
        ans = [[] for _ in range(rows)]
        for k,v in hmap.items():
            for i in range(v):
                ans[i].append(k)

        return ans
        