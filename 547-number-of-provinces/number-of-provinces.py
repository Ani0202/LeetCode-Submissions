class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        ans = 0
        visited = [False for _ in range(n)]

        def dfs(city):
            visited[city] = True
            for i in range(n):
                if isConnected[city][i] and not visited[i]:
                    dfs(i)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                ans += 1

        return ans
