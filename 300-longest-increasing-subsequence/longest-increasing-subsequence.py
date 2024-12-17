class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1 for _ in range(n)]
        ans = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[i], 1 + arr[j])
            ans = max(ans, arr[i])

        return ans
