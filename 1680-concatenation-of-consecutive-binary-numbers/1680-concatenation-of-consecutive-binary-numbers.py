class Solution:
    def concatenatedBinary(self, n: int) -> int:
        shift = 0
        ans = 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                shift += 1
            ans = ((ans << shift) | i) % 1000000007
        return ans
