class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_hrs(s):
            hrs = 0
            for count in piles:
                hrs += -(count // -s)

            return hrs

        low = -(sum(piles) // -h)
        high = max(piles)
        ans = -1
        while low <= high:
            m = (low + high) // 2
            if count_hrs(m) <= h:
                ans = m
                high = m - 1
            else:
                low = m + 1

        return ans
