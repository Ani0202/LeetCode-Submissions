class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = -1
        for i in nums:
            if nums[abs(i)-1] < 0:
                d = abs(i)
            else:
                nums[abs(i)-1] *= -1
        for i,v in enumerate(nums):
            if v > 0:
                return [d, i+1]
        