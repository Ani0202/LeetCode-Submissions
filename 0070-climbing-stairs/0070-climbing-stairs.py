class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        prev1 = 1
        prev2 = 2
        for _ in range(3, n+1):
            prev1, prev2 = prev2, prev1+prev2
        return prev2
        
        