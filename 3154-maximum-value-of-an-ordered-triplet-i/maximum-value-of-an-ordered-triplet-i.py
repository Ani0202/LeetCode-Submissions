class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        maxLeft = [0 for _ in range(n)]
        maxLeft[0] = nums[0]
        for i in range(1, n):
            maxLeft[i] = max(maxLeft[i - 1], nums[i - 1])

        maxRight = nums[n - 1]
        ans = 0
        for i in range(n - 2, 0, -1):
            ans = max(ans, (maxLeft[i] - nums[i]) * maxRight)
            maxRight = max(maxRight, nums[i])

        return ans
