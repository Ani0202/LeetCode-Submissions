class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        h = n - 1
        ans = 0
        while l <= h:
            area = min(height[l], height[h]) * (h - l)
            if ans < area:
                ans = area

            if height[l] < height[h]:
                curr = height[l]
                while l <= h and height[l] <= curr:
                    l += 1
            else:
                curr = height[h]
                while l <= h and height[h] <= curr:
                    h -= 1

        return ans
