# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dummyNode = TreeNode()
        nodeStack = [dummyNode]
        i = 0
        while i < len(traversal):
            depth = 0
            nodeVal = ""
            while traversal[i] == "-":
                depth += 1
                i += 1

            while i < len(traversal) and "0" <= traversal[i] <= "9":
                nodeVal += traversal[i]
                i += 1

            while len(nodeStack) != depth + 1:
                nodeStack.pop()

            node = nodeStack[-1]
            if node.left is None:
                node.left = TreeNode(int(nodeVal))
                nodeStack.append(node.left)
            else:
                node.right = TreeNode(int(nodeVal))
                nodeStack.append(node.right)

        return dummyNode.left
