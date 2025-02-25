class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, ans = 0, 1, 0
        MOD = 1000000007
        total = 0
        for num in arr:
            total += num
            if total % 2:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1

        return ans
