class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        n = len(nums)
        while i < 32:
            zeroes = 0
            for num in nums:
                zeroes += (num >> i) & 1

            ans += zeroes * (n - zeroes)
            i += 1

        return ans
