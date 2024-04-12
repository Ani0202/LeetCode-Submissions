class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftArr = [0 for _ in range(n)]
        for i in range(1, n):
            leftArr[i] = max(leftArr[i - 1], height[i - 1])

        ans = 0
        right = 0
        for i in range(n - 2, -1, -1):
            right = max(right, height[i + 1])
            diff = min(right, leftArr[i]) - height[i]
            ans += diff if diff > 0 else 0

        return ans
