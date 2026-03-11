class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        todo, bitmask = n, 1

        while todo > 0:
            todo >>= 1
            bitmask <<= 1

        return n ^ (bitmask - 1)
