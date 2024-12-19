class Solution:
    def findRow(self, matrix, target):
        ans = -1
        l = 0
        h = len(matrix) - 1
        while l <= h:
            m = (l + h) // 2
            if matrix[m][-1] == target:
                return m
            elif matrix[m][-1] > target:
                ans = m
                h = m - 1
            else:
                l = m + 1

        return ans

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        l = 0
        h = len(matrix[row]) - 1
        while l <= h:
            mid = (l + h) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                h = mid - 1
            else:
                l = mid + 1

        return False
