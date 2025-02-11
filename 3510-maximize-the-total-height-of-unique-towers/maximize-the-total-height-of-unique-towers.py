class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        heights = sorted(maximumHeight, reverse=True)
        allowedHeight = heights[0]
        ans = 0
        for height in heights:
            if allowedHeight <= 0:
                return -1

            acceptedHeight = min(allowedHeight, height)
            ans += acceptedHeight
            allowedHeight = acceptedHeight - 1

        return ans
