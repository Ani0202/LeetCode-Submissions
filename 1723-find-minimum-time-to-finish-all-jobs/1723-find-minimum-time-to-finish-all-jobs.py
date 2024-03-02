class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        self.workers = [0 for _ in range(k)]
        self.ans = float("inf")
        self.backTrack(0, jobs, k)
        return self.ans

    def backTrack(self, ind, jobs, k):
        if ind == len(jobs):
            self.ans = min(self.ans, max(self.workers))
            return
        for i in range(k):
            if self.workers[i] + jobs[ind] > self.ans:
                continue
            self.workers[i] += jobs[ind]
            self.backTrack(ind + 1, jobs, k)
            self.workers[i] -= jobs[ind]
            if self.workers[i] == 0:
                break
