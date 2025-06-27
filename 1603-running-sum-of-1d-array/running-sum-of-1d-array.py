class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = nums[:]
        for i in range(1, len(nums)):
            runningSum[i] += runningSum[i - 1]

        return runningSum
