class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        hmap = defaultdict(set)
        for i,t in logs:
            hmap[i].add(t)
        ans = [0 for _ in range(k)]
        for v in hmap.values():
            ans[len(v)-1] += 1
        return ans
        