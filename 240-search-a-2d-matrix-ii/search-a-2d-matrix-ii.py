class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n - 1
        while r < m and c >= 0:
            curr = matrix[r][c]
            if curr == target:
                return True
            elif curr > target:
                c -= 1
            else:
                r += 1

        return False
