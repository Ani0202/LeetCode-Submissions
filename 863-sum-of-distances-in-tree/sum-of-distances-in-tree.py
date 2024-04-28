class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Perform a depth-first search to calculate initial distances and subtree sizes
        def dfs_calculate_dist_and_size(current: int, parent: int, depth: int) -> None:
            total_distance[0] += depth
            subtree_size[current] = 1
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    dfs_calculate_dist_and_size(neighbor, current, depth + 1)
                    subtree_size[current] += subtree_size[neighbor]

        # Perform a second DFS to calculate the answer for each node based on subtree re-rooting
        def dfs_re_root(current: int, parent: int, total_dist: int) -> None:
            # The new total distance is the parent total distance
            # adjusted for moving the root from the parent to the current node
            distances[current] = total_dist
            for neighbor in adjacency_list[current]:
                if neighbor != parent:
                    new_total_dist = total_dist - subtree_size[neighbor] + (n - subtree_size[neighbor])
                    dfs_re_root(neighbor, current, new_total_dist)

        # Initialize the adjacency list to store the graph
        adjacency_list = defaultdict(list)
        # Store each pair of edges in both directions
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        # Initialize list for distances and sizes
        total_distance = [0]
        subtree_size = [0] * n
        distances = [0] * n

        # First depth-first search: Calculate total distance and subtree sizes
        dfs_calculate_dist_and_size(0, -1, 0)

        # Second depth-first search: Calculate the answer for each node
        dfs_re_root(0, -1, total_distance[0])

        return distances

        