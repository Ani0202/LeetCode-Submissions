"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""


class Solution:
    def construct(self, grid: List[List[int]]) -> "Node":
        def dfs(x, y, m, n):
            zeros = ones = 0
            for i in range(x, m + 1):
                for j in range(y, n + 1):
                    if grid[i][j] == 0:
                        zeros += 1
                    else:
                        ones += 1

            isLeaf = zeros == 0 or ones == 0
            val = isLeaf and ones == 1
            if isLeaf:
                return Node(grid[x][y], True)

            midV = (x + m) // 2
            midH = (y + n) // 2
            topLeft = dfs(x, y, midV, midH)
            topRight = dfs(x, midH + 1, midV, n)
            bottomLeft = dfs(midV + 1, y, m, midH)
            bottomRight = dfs(midV + 1, midH + 1, m, n)
            return Node(val, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(0, 0, len(grid) - 1, len(grid[0]) - 1)
