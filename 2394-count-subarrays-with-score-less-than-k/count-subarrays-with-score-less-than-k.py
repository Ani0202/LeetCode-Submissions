class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        j = 0
        total = 0
        ans = 0
        while j < n:
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1

            ans += j - i + 1
            j += 1

        return ans
