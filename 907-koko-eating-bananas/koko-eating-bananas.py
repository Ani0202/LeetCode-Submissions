class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def count_hrs(s):
            hrs = 0
            for count in piles:
                hrs += count // s
                if count % s != 0:
                    hrs += 1

            return hrs

        low = 1
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
