class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        req = [0] * numCourses
        preReq = defaultdict(list)
        for a, b in prerequisites:
            preReq[b].append(a)
            req[a] += 1

        stack = []
        for course, nReq in enumerate(req):
            if nReq == 0:
                stack.append(course)

        while stack:
            course = stack.pop()
            numCourses -= 1
            for reqCourse in preReq[course]:
                req[reqCourse] -= 1
                if req[reqCourse] == 0:
                    stack.append(reqCourse)

        return numCourses == 0
