class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        ans = 0
        hmap = defaultdict(int)
        while j < len(nums):
            hmap[nums[j]] += 1
            if hmap[nums[j]] > k:
                while nums[i] != nums[j]:
                    hmap[nums[i]] -= 1
                    i += 1
                hmap[nums[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1

        return ans
