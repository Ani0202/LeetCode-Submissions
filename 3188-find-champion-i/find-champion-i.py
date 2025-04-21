class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(n):
            champ = True
            for j in range(n):
                if i != j and grid[i][j] != 1:
                    champ = False
                    break

            if champ:
                return i

        return -1
