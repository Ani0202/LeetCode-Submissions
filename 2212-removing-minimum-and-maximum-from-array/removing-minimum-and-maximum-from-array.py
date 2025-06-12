class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        maxEle = -float("inf")
        minEle = float("inf")
        maxInd = -1
        minInd = -1
        for i, num in enumerate(nums):
            if num > maxEle:
                maxEle = num
                maxInd = i

            if num < minEle:
                minEle = num
                minInd = i

        m = min(maxInd, minInd)
        M = max(maxInd, minInd)
        return n - max(M - m - 1, m, n - M - 1)
