class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        count = 0
        prevTime = 0
        for start, end in meetings:
            if start > prevTime:
                count += start - prevTime - 1
            prevTime = max(prevTime, end)

        return count + days - prevTime
