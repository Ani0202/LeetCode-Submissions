class Solution:
    def minimumHammingDistance(
        self, source: List[int], target: List[int], allowedSwaps: List[List[int]]
    ) -> int:
        n = len(source)

        parent = [i for i in range(n)]
        rank = [1 for _ in range(n)]

        def find_parent(x):
            if parent[x] != x:
                parent[x] = find_parent(parent[x])

            return parent[x]

        def union(x, y):
            par_x = find_parent(x)
            par_y = find_parent(y)
            if par_x != par_y:
                if rank[par_x] > rank[par_y]:
                    parent[par_y] = par_x
                elif rank[par_y] > rank[par_x]:
                    parent[par_x] = par_y
                else:
                    parent[par_x] = par_y
                    rank[par_y] += 1

        for a, b in allowedSwaps:
            union(a, b)

        components = defaultdict(list)
        for i in range(n):
            root = find_parent(i)
            components[root].append(i)

        matches = 0

        for root in components:
            ind = components[root]
            source_vals = [source[i] for i in ind]
            target_vals = [target[i] for i in ind]

            source_counts = Counter(source_vals)
            target_counts = Counter(target_vals)

            intersection = source_counts & target_counts
            matches += sum(intersection.values())

        return n - matches
