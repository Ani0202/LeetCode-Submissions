# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def findSum(node, total):
            total = total * 10 + node.val
            if node.left is None and node.right is None:
                self.ans += total
                return

            if node.left:
                findSum(node.left, total)
            if node.right:
                findSum(node.right, total)

        findSum(root, 0)
        return self.ans
