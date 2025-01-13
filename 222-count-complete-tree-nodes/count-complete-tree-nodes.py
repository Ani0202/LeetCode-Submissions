# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def findDepth(node):
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        l = findDepth(root.left)
        r = findDepth(root.right)
        if l == r:
            return (1 << l) + self.countNodes(root.right)
        else:
            return (1 << r) + self.countNodes(root.left)
