class Solution:
    MOD = 10**9 + 7

    def power(self, x, n):
        if n == 0:
            return 1

        res = self.power(x, n // 2)
        if n % 2 == 0:
            return (res * res) % self.MOD
        else:
            return (x * res * res) % self.MOD

    def monkeyMove(self, n: int) -> int:
        return (self.power(2, n) - 2) % self.MOD
