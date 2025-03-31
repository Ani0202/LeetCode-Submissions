class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairSum = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pairSum.sort()
        ans = 0
        for i in range(k - 1):
            ans += pairSum[n - 2 - i] - pairSum[i]

        return ans
