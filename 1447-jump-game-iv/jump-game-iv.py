class Solution:
    def minJumps(self, arr: List[int]) -> int:
        jumps = dict()
        for i, v in enumerate(arr):
            if v not in jumps:
                jumps[v] = []

            jumps[v].append(i)

        visited = set()
        q = deque([(0, 0)])
        visited.add(0)
        while len(q):
            i, j = q.popleft()
            if i == len(arr) - 1:
                return j

            if arr[i] in jumps:
                for n in jumps[arr[i]]:
                    if n not in visited:
                        q.append((n, j + 1))
                        visited.add(n)

                del jumps[arr[i]]

            if i - 1 >= 0 and i - 1 not in visited:
                q.append((i - 1, j + 1))
                visited.add(i - 1)

            if i + 1 < len(arr) and i + 1 not in visited:
                q.append((i + 1, j + 1))
                visited.add(i + 1)

        return -1
