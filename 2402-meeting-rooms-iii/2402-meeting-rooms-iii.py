class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetCount = [0 for _ in range(n)]
        meetRoom = [0 for _ in range(n)]
        meetings.sort(key=lambda x: x[0])
        for i in meetings:
            minRoom = -1
            minCount = float("inf")
            roomFound = False
            for j in range(n):
                if meetRoom[j] <= i[0]:
                    meetRoom[j] = i[1]
                    meetCount[j] += 1
                    roomFound = True
                    break
                if meetRoom[j] < minCount:
                    minCount = meetRoom[j]
                    minRoom = j
            if roomFound == False:
                meetRoom[minRoom] = minCount + i[1] - i[0]
                meetCount[minRoom] += 1
        return meetCount.index(max(meetCount))
