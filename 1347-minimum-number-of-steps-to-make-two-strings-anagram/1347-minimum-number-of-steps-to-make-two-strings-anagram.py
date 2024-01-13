class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hmapS = defaultdict(int)
        hmapT = defaultdict(int)
        for i in range(len(s)):
            hmapS[s[i]] += 1
            hmapT[t[i]] += 1
        ans = 0
        for k,v1 in hmapS.items():
            ans += max(0, v1-hmapT[k])
        return ans