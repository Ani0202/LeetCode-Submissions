class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i]) == (s - nums[i]) / 2:
                return i

        return -1
