# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(
        self, root: Optional[TreeNode], limit: int
    ) -> Optional[TreeNode]:
        def delNodes(node, val):
            if node == None:
                return 0
            lNode = node.left
            rNode = node.right
            l = delNodes(node.left, val + node.val)
            r = delNodes(node.right, val + node.val)
            print(node.val, val, l, r)
            if val + node.val + l < limit:
                node.left = None
            if val + node.val + r < limit:
                node.right = None

            if lNode and rNode:
                return max(l, r) + node.val
            return node.val + (l if lNode else r)
        head = TreeNode()
        head.left = root
        delNodes(head, 0)
        return head.left
