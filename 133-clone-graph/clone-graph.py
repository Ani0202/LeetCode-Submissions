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
        nodes = dict()

        def addNodes(n):
            if n is None:
                return None

            val = n.val
            neigh = n.neighbors
            if val not in nodes:
                newNode = Node(val, [])
                nodes[val] = newNode
                for i in neigh:
                    newNode.neighbors.append(addNodes(i))

            return nodes[val]

        return addNodes(node)
