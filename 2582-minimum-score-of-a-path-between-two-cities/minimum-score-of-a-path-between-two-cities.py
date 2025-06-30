class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        edges = defaultdict(list)
        for a, b, dist in roads:
            edges[a].append(b)
            edges[b].append(a)

        visited = set()
        visited.add(1)
        stack = [1]
        while stack:
            city = stack.pop()
            for dest in edges[city]:
                if dest not in visited:
                    visited.add(dest)
                    stack.append(dest)

        distances = sorted(roads, key=lambda x: x[2])
        for a, b, dist in distances:
            if a in visited or b in visited:
                return dist

        return -1
