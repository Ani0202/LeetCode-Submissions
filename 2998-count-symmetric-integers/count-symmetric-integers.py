class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            if self.isSymmetric(num):
                ans += 1

        return ans

    def isSymmetric(self, num):
        strNum = str(num)
        n = len(strNum)
        if n % 2 != 0:
            return False

        return sum([int(i) for i in strNum[: n // 2]]) == sum(
            [int(i) for i in strNum[n // 2 :]]
        )
