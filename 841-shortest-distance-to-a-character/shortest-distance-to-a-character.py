class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        leftArr = []
        prevOcc = -float("inf")
        for i in range(n):
            if s[i] == c:
                prevOcc = i

            leftArr.append(prevOcc)

        prevOcc = float("inf")
        ans = [-1 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prevOcc = i

            ans[i] = min(prevOcc - i, i - leftArr[i])

        return ans
