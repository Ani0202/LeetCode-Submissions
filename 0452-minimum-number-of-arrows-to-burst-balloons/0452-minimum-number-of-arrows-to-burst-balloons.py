class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[1])
        end = points[0][1]
        ans = 1
        for i in range(1, len(points)):
            if points[i][0] > end:
                end = points[i][1]
                ans += 1

        return ans
        