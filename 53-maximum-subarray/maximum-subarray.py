class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        minTemp = 0
        curr = 0
        for num in nums:
            curr += num
            ans = max(ans, curr - minTemp)
            minTemp = min(minTemp, curr)

        return ans
