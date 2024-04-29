# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node, dir):
            if node is None:
                return -1
            l = dfs(node.left, 1)
            r = dfs(node.right, 0)
            self.ans = max(self.ans, 1 + max(l, r))
            return 1 + (l if dir == 0 else r)

        dfs(root, 0)
        return self.ans
