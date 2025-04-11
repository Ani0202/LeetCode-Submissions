class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for num in range(low, high + 1):
            strNum = str(num)
            n = len(strNum)
            if n % 2 == 0 and sum([int(i) for i in strNum[: n // 2]]) == sum(
                [int(i) for i in strNum[n // 2 :]]
            ):
                ans += 1

        return ans
