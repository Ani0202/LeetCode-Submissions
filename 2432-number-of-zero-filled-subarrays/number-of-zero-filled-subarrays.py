class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        j = 0
        while j < n:
            if nums[j] == 0:
                i = j
                while j < n and nums[j] == 0:
                    j += 1
                    ans += j - i

            j += 1

        return ans
