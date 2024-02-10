class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)

        def isAns(c):
            for i in range(n):
                if citations[i] >= c:
                    return n - i >= c
            return False

        l = 0
        h = citations[n - 1]
        ans = 0
        while l <= h:
            mid = (l + h) // 2
            if isAns(mid):
                ans = mid
                l = mid + 1
            else:
                h = mid - 1
        return ans
