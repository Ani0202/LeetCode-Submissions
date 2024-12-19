class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        h = (m * n) - 1
        while l <= h:
            mid = (l + h) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val > target:
                h = mid - 1
            else:
                l = mid + 1

        return False
