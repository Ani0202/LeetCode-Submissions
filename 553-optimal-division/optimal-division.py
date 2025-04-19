class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        elif len(nums) == 1:
            return str(nums[0])
        else:
            suff = "/".join(str(i) for i in nums[1:])
            return str(nums[0]) + "/" + "(" + suff + ")"
