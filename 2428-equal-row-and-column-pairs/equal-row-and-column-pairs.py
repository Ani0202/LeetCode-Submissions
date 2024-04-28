class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        hMap = dict()
        for i in range(n):
            s = ""
            for j in range(n):
                s += str(grid[i][j]) + "."

            hMap[s] = hMap.get(s, 0) + 1

        ans = 0
        for j in range(n):
            s = ""
            for i in range(n):
                s += str(grid[i][j]) + "."

            ans += hMap.get(s, 0)

        return ans
