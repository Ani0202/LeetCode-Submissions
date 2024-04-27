class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        ans = 0

        def bfs(ind, visited):
            visited.add(ind)
            q = deque([ind])
            while len(q):
                n = q.popleft()
                for i in range(len(isConnected)):
                    if isConnected[n][i] and i not in visited:
                        visited.add(i)
                        q.append(i)

        for i in range(n):
            if i not in visited:
                bfs(i, visited)
                ans += 1

        return ans
