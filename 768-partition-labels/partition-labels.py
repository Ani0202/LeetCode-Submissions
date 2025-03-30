class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        lastOcc = dict()
        for i in range(n):
            lastOcc[s[i]] = i

        lastInd = -1
        size = 0
        ans = []
        for i in range(n):
            size += 1
            lastInd = max(lastInd, lastOcc[s[i]])
            if lastInd == i:
                ans.append(size)
                size = 0

        return ans
