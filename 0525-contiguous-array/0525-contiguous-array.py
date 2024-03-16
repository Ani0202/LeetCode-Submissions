class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = dict()
        hmap[0] = -1
        ans = 0
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in hmap:
                ans = max(ans, i - hmap[count])
            else:
                hmap[count] = i

        return ans
        