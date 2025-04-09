class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        for u, v in adjacentPairs:
            edges[u].append(v)
            edges[v].append(u)

        curr = None
        for vert, edge in edges.items():
            if len(edge) == 1:
                curr = vert
                break

        prev = None
        visited = set()
        ans = []
        while prev != curr:
            ans.append(curr)
            visited.add(curr)
            prev = curr
            for num in edges[curr]:
                if num not in visited:
                    curr = num

        return ans
