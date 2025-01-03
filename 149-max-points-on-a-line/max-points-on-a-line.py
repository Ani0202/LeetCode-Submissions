class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        n = len(points)
        ans = 0
        for i in range(n - 1):
            hmap = dict()
            for j in range(i + 1, n):
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                hcf = gcd(dx, dy)
                key = str(dy // hcf) + "/" + str(dx // hcf)
                hmap[key] = hmap.get(key, 0) + 1
                ans = max(ans, hmap[key])

        return ans + 1
