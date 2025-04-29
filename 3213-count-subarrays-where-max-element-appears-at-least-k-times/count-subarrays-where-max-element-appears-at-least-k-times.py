class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        maxEle = max(nums)
        maxArr = []
        ans = 0
        for i in range(n):
            if nums[i] == maxEle:
                maxArr.append(i)
            if len(maxArr) >= k:
                ans += maxArr[-k] + 1

        return ans
