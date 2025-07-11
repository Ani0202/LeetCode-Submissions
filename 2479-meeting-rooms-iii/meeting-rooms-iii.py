class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        availRooms = list(range(n))
        unAvailRooms = []
        noOfMeetings = [0] * n
        for start, end in sorted(meetings):
            while unAvailRooms and unAvailRooms[0][0] <= start:
                endTime, room = heapq.heappop(unAvailRooms)
                heapq.heappush(availRooms, room)

            if availRooms:
                room = heapq.heappop(availRooms)
                heapq.heappush(unAvailRooms, (end, room))
                noOfMeetings[room] += 1
            else:
                endTime, room = heapq.heappop(unAvailRooms)
                heapq.heappush(unAvailRooms, (end + endTime - start, room))
                noOfMeetings[room] += 1

        maxMeetings = -1
        maxMeetingsRoom = -1
        for i, v in enumerate(noOfMeetings):
            if v > maxMeetings:
                maxMeetings = v
                maxMeetingsRoom = i

        return maxMeetingsRoom
