class Solution:
    def reverseBits(self, n: int) -> int:
        i = 0
        ans = 0
        while i < 32:
            if n & 1:
                ans += 2**(31-i)
            n = n >> 1
            i += 1

        return ans
        