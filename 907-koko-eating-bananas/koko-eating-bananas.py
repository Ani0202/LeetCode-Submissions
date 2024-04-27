class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(speed):
            hrs = 0
            for num in piles:
                hrs += num // speed
                hrs += 1 if num % speed != 0 else 0

            return hrs <= h

        low = 1
        high = max(piles)
        ans = 0
        while low <= high:
            mid = (low + high) >> 1
            if isValid(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
