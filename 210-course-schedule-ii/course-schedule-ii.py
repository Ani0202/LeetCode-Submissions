class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        req = [0] * numCourses
        preReq = defaultdict(list)
        ans = []
        for a, b in prerequisites:
            preReq[b].append(a)
            req[a] += 1

        stack = []
        for course, nReq in enumerate(req):
            if nReq == 0:
                stack.append(course)

        while stack:
            course = stack.pop()
            ans.append(course)
            numCourses -= 1
            for reqCourse in preReq[course]:
                req[reqCourse] -= 1
                if req[reqCourse] == 0:
                    stack.append(reqCourse)

        return ans if numCourses == 0 else []
