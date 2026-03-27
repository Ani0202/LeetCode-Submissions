class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if res > INT_MAX // 10:
                return 0

            if res == INT_MAX // 10:
                if sign == 1 and pop > 7:
                    return 0
                if sign == -1 and pop > 8:
                    return 0

            res = res * 10 + pop

        return res * sign
