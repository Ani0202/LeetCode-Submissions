class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        req = (n * (n + 1)) // 2
        act = sum(nums)
        return req - act
