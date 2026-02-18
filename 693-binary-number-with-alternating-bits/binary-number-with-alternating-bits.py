class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n & 1
        for i in range(1, 32):
            curr = n >> i
            if curr == 0:
                break

            curr &= 1

            if curr == prev:
                return False

            prev = curr

        return True
