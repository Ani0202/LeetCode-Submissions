class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda x: (int(x[1]), x[0] != "OFFLINE"))
        online = [0] * numberOfUsers
        mentions = [0] * numberOfUsers
        for message, timeStamp, mention in events:
            time = int(timeStamp)
            if message == "MESSAGE":
                if mention == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1
                elif mention == "HERE":
                    for i in range(numberOfUsers):
                        mentions[i] += 1 if online[i] <= time else 0
                else:
                    for i in mention.split():
                        mentions[int(i[2:])] += 1

            elif message == "OFFLINE":
                online[int(mention)] = time + 60

        return mentions
