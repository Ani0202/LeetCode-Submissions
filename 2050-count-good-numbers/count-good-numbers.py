class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return self.findPow(5, (n + 1) // 2) * self.findPow(4, n // 2) % 1000000007

    def findPow(self, x, y):
        ans, mul = 1, x
        while y > 0:
            if y % 2 == 1:
                ans = ans * mul % 1000000007

            mul = mul * mul % 1000000007
            y //= 2

        return ans
