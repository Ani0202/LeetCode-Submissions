class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return grid[0][0]

        minInd = -1
        arr = [float("inf"), float("inf")]
        for i,v in enumerate(grid[0]):
            if v <= arr[0]:
                arr[1] = arr[0]
                arr[0] = v
                minInd = i
            elif v < arr[1]:
                arr[1] = v

        dp = grid[0]
        for i in range(1, n):
            temp = [float("inf"), float("inf")]
            tempMinInd = -1
            for j in range(n):
                if j == minInd:
                    dp[j] = grid[i][j] + arr[1]
                else:
                    dp[j] = grid[i][j] + arr[0]

                if dp[j] <= temp[0]:
                    temp[1] = temp[0]
                    temp[0] = dp[j]
                    tempMinInd = j
                elif dp[j] < temp[1]:
                    temp[1] = dp[j]

            arr = temp
            minInd = tempMinInd
            
        return arr[0]