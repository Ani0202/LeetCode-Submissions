class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)
        for num in nums:
            hmap[num] += 1
        ans = [0,0]
        for v in hmap.values():
            ans[0] += v//2
            ans[1] += v%2
        return ans
        