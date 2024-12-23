class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        l = 0
        h = n - 1
        while l <= h:
            m = l + (h - l) // 2
            if m == 0:
                if nums[m] > nums[m + 1]:
                    return m
                else:
                    l = m + 1
            elif m == n - 1:
                if nums[m] > nums[m - 1]:
                    return m
                else:
                    h = m - 1
            elif nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] > nums[m - 1]:
                l = m + 1
            else:
                h = m - 1
