class Solution:
    def findIndex(self, nums, target, limit):
        l = 0
        h = len(nums) - 1
        ans = -1
        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                ans = m
                if limit == "lower":
                    h = m - 1
                else:
                    l = m + 1

            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [
            self.findIndex(nums, target, "lower"),
            self.findIndex(nums, target, "upper"),
        ]
