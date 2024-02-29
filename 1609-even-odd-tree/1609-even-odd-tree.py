# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while len(q):
            n = len(q)
            if level % 2 == 0:
                prev = q.popleft()
                if prev.val % 2 == 0:
                    return False
                if prev.left:
                    q.append(prev.left)
                if prev.right:
                    q.append(prev.right)
                while n - 1:
                    node = q.popleft()
                    if node.val <= prev.val or node.val % 2 == 0:
                        return False
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    prev = node
                    n -= 1
            else:
                prev = q.popleft()
                if prev.val % 2 != 0:
                    return False
                if prev.left:
                    q.append(prev.left)
                if prev.right:
                    q.append(prev.right)
                while n - 1:
                    node = q.popleft()
                    if node.val >= prev.val or node.val % 2 != 0:
                        return False
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                    prev = node
                    n -= 1
            level += 1

        return True
