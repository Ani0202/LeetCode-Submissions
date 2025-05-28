class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        def buildGraph(edges, i):
            graph = [[] for _ in range(i)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            return graph

        graph1 = buildGraph(edges1, n)
        graph2 = buildGraph(edges2, m)

        def dfs(node, parent, depth, graph):
            if depth < 0:
                return 0

            count = 1
            for child in graph[node]:
                if child != parent:
                    count += dfs(child, node, depth - 1, graph)

            return count

        targetNodes2 = max(dfs(i, -1, k - 1, graph2) for i in range(m))

        return [dfs(i, -1, k, graph1) + targetNodes2 for i in range(n)]
