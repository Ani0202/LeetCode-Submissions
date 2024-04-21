class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj = dict()
        for s, d in edges:
            if s not in adj:
                adj[s] = []

            if d not in adj:
                adj[d] = []

            adj[s].append(d)
            adj[d].append(s)

        stack = [source]
        visited = set()
        while len(stack):
            n = stack.pop()
            if n == destination:
                return True

            visited.add(n)
            for e in adj[n]:
                if e not in visited:
                    stack.append(e)

        return False
