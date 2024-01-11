class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [i for i in range(n+1)]
        for i in range(2, len(nums)):
            if i%2:
                nums[i] = nums[(i-1)//2] + nums[((i-1)//2) + 1]
            else:
                nums[i] = nums[i//2]

        return max(nums)