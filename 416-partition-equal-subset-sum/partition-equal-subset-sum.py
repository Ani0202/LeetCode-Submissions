class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = {0}
        for num in nums:
            new_sums = {x + num for x in dp}
            dp.update(new_sums)
            if target in dp:
                return True

        return False
