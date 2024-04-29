class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        lArr = [float("inf") for _ in range(n)]
        rArr = [-float("inf") for _ in range(n)]
        for i in range(1, n):
            lArr[i] = min(lArr[i - 1], nums[i - 1])
            rArr[n - i - 1] = max(rArr[n - i], nums[n - i])

        for i in range(n):
            if lArr[i] < nums[i] < rArr[i]:
                return True

        return False
