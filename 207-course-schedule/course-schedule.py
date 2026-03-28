class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req = defaultdict(int)
        pre_cour = defaultdict(list)
        for a, b in prerequisites:
            pre_req[a] += 1
            pre_cour[b].append(a)

        queue = deque()
        courses_taken = 0
        for i in range(numCourses):
            if pre_req[i] == 0:
                queue.append(i)

        while queue:
            sub = queue.popleft()
            courses_taken += 1
            for course in pre_cour[sub]:
                pre_req[course] -= 1
                if pre_req[course] == 0:
                    queue.append(course)

        return courses_taken == numCourses
