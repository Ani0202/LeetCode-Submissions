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
        ans = [curr]
        while len(ans) < len(edges):
            for num in edges[curr]:
                if num != prev:
                    ans.append(num)
                    prev = curr
                    curr = num
                    break

        return ans
