class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_before = [0 for _ in range(n)]
        for i in range(1, n):
            max_before[i] = max(max_before[i - 1], height[i - 1])

        max_after = height[n - 1]
        ans = 0
        for i in range(n - 2, -1, -1):
            max_len = min(max_after, max_before[i])
            max_after = max(max_after, height[i])
            if height[i] < max_len:
                ans += max_len - height[i]

        return ans
