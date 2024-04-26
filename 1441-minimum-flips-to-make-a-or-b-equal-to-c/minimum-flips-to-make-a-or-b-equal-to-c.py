class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            A = (a >> i) & 1
            B = (b >> i) & 1
            C = (c >> i) & 1
            if C == 0:
                ans += A + B
            else:
                if A | B == 0:
                    ans += 1

        return ans
