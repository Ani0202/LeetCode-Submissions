class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings_x = defaultdict(list)
        buildings_y = defaultdict(list)

        for x, y in buildings:
            buildings_x[x].append(y)
            buildings_y[y].append(x)

        for x in buildings_x:
            buildings_x[x].sort()

        for y in buildings_y:
            buildings_y[y].sort()

        ans = 0

        for x, y in buildings:
            x_build = buildings_y[y]
            y_build = buildings_x[x]

            if x_build[0] < x < x_build[-1] and y_build[0] < y < y_build[-1]:
                ans += 1

        return ans
