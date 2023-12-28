"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.hmap = dict()
        if node == None:
            return None
        return self.dfs(node)

    def dfs(self, node):
        if node.val in self.hmap:
            return self.hmap[node.val]

        newNode = Node(node.val, [])
        self.hmap[node.val] = newNode
        for i in node.neighbors:
            newNode.neighbors.append(self.dfs(i))

        return newNode
        