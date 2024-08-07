class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0

        nums.sort()
        ans = float("inf")
        for left in range(4):
            ans = min(ans, nums[n - 4 + left] - nums[left])

        return ans
