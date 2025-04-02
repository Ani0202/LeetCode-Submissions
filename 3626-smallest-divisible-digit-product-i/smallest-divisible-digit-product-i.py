class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while num >= n:
            temp = num
            prod = 1
            while temp:
                prod *= temp % 10
                temp //= 10
                if prod == 0:
                    break

            if prod % t == 0:
                return num

            num += 1

        return -1
