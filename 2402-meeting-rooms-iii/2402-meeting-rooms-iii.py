class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        used = []
        unused = list(range(n))
        meetCount = [0 for _ in range(n)]
        for s, e in sorted(meetings):
            while used and used[0][0] <= s:
                end, room = heappop(used)
                heappush(unused, room)
            if unused:
                room = heappop(unused)
                heappush(used, [e, room])
            else:
                end, room = heappop(used)
                heappush(used, [end + e - s, room])
            meetCount[room] += 1

        return meetCount.index(max(meetCount))
