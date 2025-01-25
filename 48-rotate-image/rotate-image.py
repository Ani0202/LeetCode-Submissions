class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][n - i - 1]
                matrix[n - j - 1][n - i - 1] = temp

        for i in range(n // 2):
            for j in range(n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - i - 1][j]
                matrix[n - i - 1][j] = temp
