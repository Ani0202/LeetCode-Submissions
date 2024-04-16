# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        q = deque([root])
        while depth > 2:
            n = len(q)
            for _ in range(n):
                N = q.popleft()
                if N.left:
                    q.append(N.left)
                if N.right:
                    q.append(N.right)
            depth -= 1
        for N in q:
            node = TreeNode(val)
            node.left = N.left
            N.left = node
            node = TreeNode(val)
            node.right = N.right
            N.right = node
        return root
