class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hmap = defaultdict(int)
        for i in nums:
            hmap[i] += 1
        ans = sorted(nums, key=lambda x: (hmap[x], -x))
        return ans
        
        