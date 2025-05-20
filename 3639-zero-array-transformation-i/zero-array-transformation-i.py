class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        change = [0 for _ in range(n + 1)]
        for l, r in queries:
            change[l] -= 1
            change[r + 1] += 1

        x = 0
        for i in range(n):
            x += change[i]
            if nums[i] + x > 0:
                return False

        return True
