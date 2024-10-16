class Solution:
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        n = len(points)
        for i in range(n - 1):
            x, y = points[i]
            slopes = defaultdict(int)
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dx = x2 - x
                dy = y2 - y
                hcf = self.gcd(dx, dy)
                slopes[(dx // hcf, dy // hcf)] += 1
                ans = max(ans, slopes[(dx // hcf, dy // hcf)])

        return ans + 1
