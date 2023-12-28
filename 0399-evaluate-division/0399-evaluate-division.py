class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def findParent(x):
            if parent[x] != x:
                parX = parent[x]
                parent[x] = findParent(parent[x])
                ratio[x] *= ratio[parX]
            return parent[x]
        ratio = defaultdict(lambda: 1.0)
        parent = defaultdict(str)
        for a, b in equations:
            parent[a], parent[b] = a, b
        for i, value in enumerate(values):
            a, b = equations[i]
            parA, parB = findParent(a), findParent(b)
          
            if parA != parB:
                parent[parA] = parB
                ratio[parA] = ratio[b] * value / ratio[a]
        results = []
        for c, d in queries:
            if c not in parent or d not in parent or findParent(c) != findParent(d):
                results.append(-1.0)
            else:
                results.append(ratio[c] / ratio[d])
              
        return results
