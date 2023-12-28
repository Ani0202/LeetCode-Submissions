class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[b].append(a)
            inDegree[a] +=1

        queue = []
        for i,v in enumerate(inDegree):
            if v == 0:
                queue.append(i)

        while queue:
            course = queue.pop()
            for i in graph[course]:
                inDegree[i] -= 1
                if inDegree[i] == 0:
                    queue.append(i)

            numCourses -= 1

        return numCourses == 0

        