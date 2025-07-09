class Solution:
    def maxFreeTime(
        self, eventTime: int, k: int, startTime: List[int], endTime: List[int]
    ) -> int:
        n = len(startTime)
        ans = 0
        total = [0 for _ in range(n + 1)]
        for i in range(n):
            total[i + 1] = total[i] + endTime[i] - startTime[i]

        for i in range(k - 1, n):
            r = eventTime if i == n - 1 else startTime[i + 1]
            l = 0 if i == k - 1 else endTime[i - k]
            ans = max(ans, r - l - total[i + 1] + total[i - k + 1])

        return ans
