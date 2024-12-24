class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        h = x
        ans = -1
        while l <= h:
            m = l + (h - l) // 2
            sqr = m * m
            if sqr == x:
                return m
            elif sqr < x:
                ans = m
                l = m + 1
            else:
                h = m - 1

        return ans
