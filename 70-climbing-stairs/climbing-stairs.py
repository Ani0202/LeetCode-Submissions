class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a = 1
        b = 2
        for _ in range(2, n):
            c = a + b
            a = b
            b = c

        return c
