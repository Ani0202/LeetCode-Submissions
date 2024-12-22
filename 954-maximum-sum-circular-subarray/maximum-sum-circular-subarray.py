class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        maxSum = nums[0]
        minSum = nums[0]
        total = 0
        for num in nums:
            currMax = max(currMax, 0) + num
            maxSum = max(maxSum, currMax)
            currMin = min(currMin, 0) + num
            minSum = min(minSum, currMin)
            total += num

        if total == minSum:
            return maxSum

        return max(maxSum, total - minSum)
