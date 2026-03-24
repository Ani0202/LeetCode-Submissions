# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def find_node(node):
            if node is None:
                return None

            if node == p or node == q:
                return node

            l = find_node(node.left)
            r = find_node(node.right)
            if l is None:
                return r
            elif r is None:
                return l
            else:
                return node

        return find_node(root)
