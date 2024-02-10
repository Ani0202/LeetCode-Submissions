class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l = 0
        n = len(citations)
        h = n
        ans = 0
        while l < h:
            mid = (l+h)//2
            print(mid)
            if citations[n-1-mid]>=mid:
                l = mid+1
                ans = mid+1
            else:
                h = mid-1
        return ans
        