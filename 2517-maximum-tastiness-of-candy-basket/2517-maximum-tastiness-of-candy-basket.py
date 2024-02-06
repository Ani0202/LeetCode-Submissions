class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        def isValid(p):
            count, previousPrice = 0, -p
            for currentPrice in price:
                if currentPrice - previousPrice >= p:
                    previousPrice = currentPrice
                    count += 1
            return count >= k

        l = 0
        r = price[-1] - price[0]
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if isValid(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1

        return ans
        