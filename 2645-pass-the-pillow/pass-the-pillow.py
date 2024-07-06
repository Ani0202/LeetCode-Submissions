class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rounds = time // (n - 1)
        extra = time % (n - 1)
        return extra + 1 if rounds % 2 == 0 else n - extra
