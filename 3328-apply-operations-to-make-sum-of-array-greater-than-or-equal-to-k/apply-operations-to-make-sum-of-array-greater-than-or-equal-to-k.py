class Solution:
    def minOperations(self, k: int) -> int:
        ans = float("inf")
        for i in range(1, k + 1):
            ans = min(ans, i - 2 + math.ceil(k / i))

        return ans
