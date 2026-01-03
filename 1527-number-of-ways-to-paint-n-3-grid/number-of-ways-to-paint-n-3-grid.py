class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 1000000007
        abc = 6
        aba = 6
        for _ in range(n - 1):
            new_abc = (2 * abc + 2 * aba) % mod
            new_aba = (2 * abc + 3 * aba) % mod
            abc = new_abc
            aba = new_aba

        return (abc + aba) % mod
