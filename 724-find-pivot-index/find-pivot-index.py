class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        sL = 0
        for i in range(len(nums)):
            if sL == (s - nums[i]) / 2:
                return i
            sL += nums[i]

        return -1
