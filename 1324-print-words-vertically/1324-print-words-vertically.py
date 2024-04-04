class Solution:
    def printVertically(self, s: str) -> List[str]:
        l = 0
        s = s.split()
        for i in s:
            l = max(l, len(i))

        ans = ["" for _ in range(l)]
        for i in range(l):
            for j in s:
                if i <= len(j) - 1:
                    ans[i] += j[i]
                else:
                    ans[i] += " "
            ans[i] = ans[i].rstrip()
        return ans
