class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for centerPoint in points:
            distMap = defaultdict(int)
            for point in points:
                squrDist = (centerPoint[0] - point[0]) ** 2 + (
                    centerPoint[1] - point[1]
                ) ** 2
                distMap[squrDist] += 1

            for val in distMap.values():
                count += val * (val - 1)

        return count
