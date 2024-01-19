class Solution:
    def trailingZeroes(self, n: int) -> int:
        d = 5
        ans = 0
        while d <= n:
            ans += n//d
            d *= 5
        return ans
        