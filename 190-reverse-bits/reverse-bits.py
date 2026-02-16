class Solution:
    def reverseBits(self, n: int) -> int:
        reversed_str = ""
        for i in range(32):
            reversed_str += str(n >> i & 1)

        return int(reversed_str, 2)
