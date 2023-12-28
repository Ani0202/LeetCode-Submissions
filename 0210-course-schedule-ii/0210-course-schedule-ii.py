class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        inDegree = [0] * numCourses
        for a,b in prerequisites:
            graph[b].append(a)
            inDegree[a] += 1

        ans = []
        queue = []
        for i,v in enumerate(inDegree):
            if v == 0:
                queue.append(i)
        while queue:
            course = queue.pop()
            for x in graph[course]:
                inDegree[x] -= 1
                if inDegree[x] == 0:
                    queue.append(x)

            numCourses -= 1
            ans.append(course)
        return ans if numCourses == 0 else []