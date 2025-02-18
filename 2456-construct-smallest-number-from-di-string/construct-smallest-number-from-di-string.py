class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        isUsed = [False for _ in range(10)]
        for i in range(1, 10):
            if self.findStr(ans, isUsed, pattern, i):
                return "".join(str(i) for i in ans)

    def findStr(self, ans, isUsed, pattern, i):
        if isUsed[i]:
            return False

        isUsed[i] = True
        ans.append(i)
        if len(ans) == len(pattern) + 1:
            return True

        dirc = pattern[len(ans) - 1]
        if dirc == "I":
            for j in range(i + 1, 10):
                if self.findStr(ans, isUsed, pattern, j):
                    return True
        else:
            for j in range(i - 1, 0, -1):
                if self.findStr(ans, isUsed, pattern, j):
                    return True

        isUsed[i] = False
        ans.pop()
        return False
