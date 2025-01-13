class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while nums[l] > nums[h]:
            mid = (l + h) // 2
            if nums[mid] < nums[l]:
                h = mid
            else:
                l = mid + 1

        return nums[l]
