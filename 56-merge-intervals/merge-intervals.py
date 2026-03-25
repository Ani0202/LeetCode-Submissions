class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        n = len(intervals)
        i = 0
        while i < n:
            start, end = intervals[i]
            j = i + 1
            while j < n and intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1

            ans.append([start, end])
            i = j

        return ans
