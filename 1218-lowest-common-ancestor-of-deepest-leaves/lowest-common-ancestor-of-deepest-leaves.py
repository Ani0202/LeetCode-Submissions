# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return (0, None)

            leftDepth, leftLca = dfs(node.left)
            rightDepth, rightLca = dfs(node.right)
            if leftDepth > rightDepth:
                return (leftDepth + 1, leftLca)
            elif rightDepth > leftDepth:
                return (rightDepth + 1, rightLca)
            else:
                return (leftDepth + 1, node)

        depth, lca = dfs(root)
        return lca
