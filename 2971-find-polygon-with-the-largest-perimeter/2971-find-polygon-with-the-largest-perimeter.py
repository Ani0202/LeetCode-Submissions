class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        s = nums[0]+nums[1]
        for i in range(2, len(nums)):
            if s > nums[i]:
                ans = s + nums[i]
            s += nums[i]

        return ans
        