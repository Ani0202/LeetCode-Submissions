class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        minIdx = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[minIdx] > k:
                ans += 1
                minIdx = i

        return ans + 1
