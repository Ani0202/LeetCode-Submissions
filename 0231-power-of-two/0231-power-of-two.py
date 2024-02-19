class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        while not (n & 1):
            n >>= 1
        return not n >> 1
