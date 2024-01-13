class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        edgesList = [[] for _ in range(n)]
        for a,b in edges:
            edgesList[a].append(b)
            edgesList[b].append(a)
        visited = [0 for _ in range(n)]
        for node in restricted:
            visited[node] = 1

        def dfs(node):
            if visited[node]:
                return 0
            visited[node] = 1
            ans = 1
            for child in edgesList[node]:
                ans += dfs(child)
            return ans

        return dfs(0)