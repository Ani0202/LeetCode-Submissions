class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        start = str(start - 1)
        finish = str(finish)
        return self.findPowNums(finish, s, limit) - self.findPowNums(start, s, limit)

    def findPowNums(self, x: str, s: str, limit: int) -> int:
        if len(x) < len(s):
            return 0

        if len(x) == len(s):
            if x >= s:
                return 1
            else:
                return 0

        suffix = x[len(x) - len(s) :]
        count = 0
        preLen = len(x) - len(s)

        for i in range(preLen):
            if limit < int(x[i]):
                count += (limit + 1) ** (preLen - i)
                return count

            count += int(x[i]) * (limit + 1) ** (preLen - 1 - i)

        if suffix >= s:
            count += 1

        return count
