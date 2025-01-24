class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        dire = 0
        ans = []
        while left <= right and top <= bottom:
            if dire == 0:
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])

                top += 1
            elif dire == 1:
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])

                right -= 1
            elif dire == 2:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])

                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])

                left += 1

            dire = (dire + 1) % 4

        return ans
