# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def findSeq(node):
            if node is None:
                return []
            elif node.left is None and node.right is None:
                return [node.val]

            return findSeq(node.left)[:] + findSeq(node.right)[:]

        leafSeq1 = findSeq(root1)
        leafSeq2 = findSeq(root2)
        if len(leafSeq1) != len(leafSeq2):
            return False

        for i in range(len(leafSeq1)):
            if leafSeq1[i] != leafSeq2[i]:
                return False

        return True
