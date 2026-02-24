# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def find_sum(node, curr):
            curr += str(node.val)
            if node.left is None and node.right is None:
                self.ans += int(curr, 2)
                return

            if node.left:
                find_sum(node.left, curr)

            if node.right:
                find_sum(node.right, curr)

        find_sum(root, "")
        return self.ans
