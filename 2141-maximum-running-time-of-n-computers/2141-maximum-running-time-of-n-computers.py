class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l = min(batteries)
        h = sum(batteries)
        ans = 0
        while l <= h:
            m = (l + h) // 2
            t = sum(min(p, m) for p in batteries)
            if t >= n * m:
                ans = m
                l = m + 1
            else:
                h = m - 1
        return ans
