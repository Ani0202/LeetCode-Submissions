"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        hmap = dict()
        for emp in employees:
            hmap[emp.id] = emp
        queue = deque([hmap[id]])
        ans = 0
        while queue:
            n = len(queue)
            for i in range(n):
                emp = queue.popleft()
                ans += emp.importance
                queue.extend([hmap[empId] for empId in emp.subordinates])

        return ans
            
        