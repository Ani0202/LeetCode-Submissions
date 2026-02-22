class Solution:
    def binaryGap(self, n: int) -> int:
        j = None
        ans = 0
        for i in range(32):
            if (n >> i) & 1:
                if j is not None:
                    ans = max(ans, i - j)

                j = i

        return ans
