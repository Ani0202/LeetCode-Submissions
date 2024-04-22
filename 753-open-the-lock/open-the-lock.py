class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        q = deque([("0000", 0)])
        deadends.add("0000")
        while len(q):
            key, steps = q.popleft()
            if key == target:
                return steps

            steps += 1
            for i in range(4):
                nextNum = key[:i] + str((int(key[i]) + 1) % 10) + key[i + 1 :]
                if nextNum not in deadends:
                    deadends.add(nextNum)
                    q.append([nextNum, steps])

                prevNum = key[:i] + str((int(key[i]) - 1) % 10) + key[i + 1 :]
                if prevNum not in deadends:
                    deadends.add(prevNum)
                    q.append([prevNum, steps])

        return -1
