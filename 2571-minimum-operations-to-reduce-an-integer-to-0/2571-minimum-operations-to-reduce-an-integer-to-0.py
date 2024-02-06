class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        count = 0
        while n:
            if n & 1:
                count += 1
            elif count:
                ans += 1
                count = 0 if count == 1 else 1
            n >>= 1

        if count == 1:
            ans += 1
        elif count > 1:
            ans += 2
        return ans
        