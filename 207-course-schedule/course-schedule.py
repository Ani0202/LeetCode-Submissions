class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            edges[b].append(a)

        states = [0 for _ in range(numCourses)]

        def has_cycle(node):
            if states[node] == 1:
                return True

            if states[node] == 2:
                return False

            states[node] = 1
            for neigh in edges[node]:
                if has_cycle(neigh):
                    return True

            states[node] = 2
            return False

        for i in range(numCourses):
            if states[i] == 0:
                if has_cycle(i):
                    return False

        return True
