# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root) >= 0

    def height(self, node):
        if node is None:
            return 0

        lHeight = self.height(node.left)
        rHeight = self.height(node.right)
        if lHeight == -1 or rHeight == -1 or abs(lHeight - rHeight) > 1:
            return -1

        return 1 + max(lHeight, rHeight)
