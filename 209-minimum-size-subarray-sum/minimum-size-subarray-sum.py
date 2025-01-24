class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = float("inf")
        total = 0
        for j in range(n):
            total += nums[j]
            while i <= j and total >= target:
                ans = min(ans, j - i + 1)
                total -= nums[i]
                i += 1

        return 0 if ans == float("inf") else ans
