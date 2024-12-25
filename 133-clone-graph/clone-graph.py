"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        self.hmap = dict()
        return self.dfs(node)

    def dfs(self, node):
        if node is None:
            return None

        if node.val in self.hmap:
            return self.hmap[node.val]

        self.hmap[node.val] = Node(node.val, [])
        for neigh in node.neighbors:
            self.hmap[node.val].neighbors.append(self.dfs(neigh))

        return self.hmap[node.val]
