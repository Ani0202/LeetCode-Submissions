# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.hMap = {0: 1}
        self.ans = 0

        def dfs(node, curr):
            if node is None:
                return
            temp = curr + node.val
            self.ans += self.hMap.get(temp - targetSum, 0)
            self.hMap[temp] = self.hMap.get(temp, 0) + 1
            dfs(node.left, temp)
            dfs(node.right, temp)
            self.hMap[temp] = self.hMap.get(temp, 1) - 1

        dfs(root, 0)
        return self.ans
