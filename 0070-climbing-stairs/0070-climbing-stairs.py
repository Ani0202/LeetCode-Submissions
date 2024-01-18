class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 0
        prev2 = 1
        for _ in range(n):
            prev1, prev2 = prev2, prev1+prev2
        return prev2
        
        