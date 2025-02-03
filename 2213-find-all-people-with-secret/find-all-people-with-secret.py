class Solution:
    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        graph = defaultdict(list)
        for x, y, t in meetings:
            graph[x].append((y, t))
            graph[y].append((x, t))

        time = [float("inf")] * n
        time[0] = 0
        time[firstPerson] = 0
        queue = deque()
        queue.append((0, 0))
        queue.append((firstPerson, 0))
        ans = {0, firstPerson}
        while queue:
            p, t = queue.popleft()
            for pn, tn in graph[p]:
                if tn >= t and time[pn] > tn:
                    time[pn] = tn
                    queue.append((pn, tn))
                    ans.add(pn)

        return list(ans)
