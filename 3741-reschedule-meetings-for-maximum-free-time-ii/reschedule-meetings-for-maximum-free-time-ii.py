class Solution:
    def maxFreeTime(
        self, eventTime: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        maxPrev = [0] * n
        maxPrev[0] = startTime[0]
        for i in range(1, n):
            maxPrev[i] = max(maxPrev[i - 1], startTime[i] - endTime[i - 1])

        maxNext = [0] * n
        maxNext[n - 1] = eventTime - endTime[n - 1]
        for i in range(n - 2, -1, -1):
            maxNext[i] = max(maxNext[i + 1], startTime[i + 1] - endTime[i])

        ans = 0
        for i in range(n):
            maxLeft = maxPrev[i] if i == 0 else startTime[i] - endTime[i - 1]

            maxRight = maxNext[i] if i == n - 1 else startTime[i + 1] - endTime[i]

            interval = 0
            if (
                i != 0
                and maxPrev[i - 1] >= (endTime[i] - startTime[i])
                or i != n - 1
                and maxNext[i + 1] >= (endTime[i] - startTime[i])
            ):
                interval = endTime[i] - startTime[i]

            ans = max(ans, maxLeft + interval + maxRight)

        return ans
