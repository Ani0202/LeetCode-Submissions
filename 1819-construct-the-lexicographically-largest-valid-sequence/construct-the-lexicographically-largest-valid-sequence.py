class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        usedNums = [False] * (n + 1)
        self.findSeq(0, ans, usedNums, n)
        return ans

    def findSeq(self, ind, ans, usedNums, n):
        if ind == len(ans):
            return True

        if ans[ind] != 0:
            return self.findSeq(ind + 1, ans, usedNums, n)

        for i in range(n, 0, -1):
            if usedNums[i]:
                continue

            usedNums[i] = True
            ans[ind] = i
            if i == 1:
                if self.findSeq(ind + 1, ans, usedNums, n):
                    return True
            elif ind + i < len(ans) and ans[ind + i] == 0:
                ans[ind + i] = i
                if self.findSeq(ind + 1, ans, usedNums, n):
                    return True

                ans[ind + i] = 0

            usedNums[i] = False
            ans[ind] = 0

        return False
