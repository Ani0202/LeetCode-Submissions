class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pairs = 0
        i = -1
        hmap = defaultdict(int)
        ans = 0
        for num in nums:
            while pairs < k and i + 1 < n:
                i += 1
                pairs += hmap[nums[i]]
                hmap[nums[i]] += 1

            if pairs >= k:
                ans += n - i

            hmap[num] -= 1
            pairs -= hmap[num]

        return ans
