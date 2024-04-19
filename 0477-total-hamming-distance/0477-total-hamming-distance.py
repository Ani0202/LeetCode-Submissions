class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            ones = 0
            zeros = 0
            for i in range(len(nums)):
                if nums[i] & 1:
                    ones += 1
                else:
                    zeros += 1

                nums[i] = nums[i] >> 1

            ans += ones * zeros
        return ans
