class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        n = len(nums)
        ans = [0 for i in range(n)]
        for k in range(n):
            if nums[k] > 0:
                ans[i] = nums[k]
                i += 2
            else:
                ans[j] = nums[k]
                j += 2

        return ans