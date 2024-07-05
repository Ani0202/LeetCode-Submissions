class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] > target:
                break
            elif matrix[i][n - 1] < target:
                continue

            for j in range(n):
                if matrix[0][j] > target:
                    break
                elif matrix[m - 1][j] < target:
                    continue
                elif matrix[i][j] == target:
                    return True

        return False
