class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        points_y = defaultdict(int)
        MOD = 1000000007
        ans = 0
        edges = 0
        for point in points:
            points_y[point[1]] += 1

        for total_points in points_y.values():
            curr_edges = total_points * (total_points - 1) // 2
            ans = (ans + curr_edges * edges) % MOD
            edges = (edges + curr_edges) % MOD

        return ans
