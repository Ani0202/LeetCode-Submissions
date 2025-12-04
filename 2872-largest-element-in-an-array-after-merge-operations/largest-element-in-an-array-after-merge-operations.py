class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        i = n - 1
        while i >= 0:
            temp = nums[i]
            j = i - 1
            while j >= 0 and nums[j] <= temp:
                temp += nums[j]
                j -= 1

            ans = max(ans, temp)
            i = j

        return ans
