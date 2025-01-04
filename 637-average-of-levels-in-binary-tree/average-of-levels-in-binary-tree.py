# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            n = len(queue)
            i = 0
            total = 0
            while i < n:
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                i += 1

            ans.append(total / n)

        return ans
