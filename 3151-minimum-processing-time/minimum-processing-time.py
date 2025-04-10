class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        n = len(processorTime)
        processorTime.sort()
        tasks.sort()
        maxTasks = []
        for i in range(4 * n):
            if i % 4 == 3:
                maxTasks.append(tasks[i])

        ans = 0
        for i in range(n):
            ans = max(ans, processorTime[i] + maxTasks[n - 1 - i])

        return ans
