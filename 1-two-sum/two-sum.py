class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_ints = dict()
        for i, num in enumerate(nums):
            if target - num in prev_ints:
                return [prev_ints[target - num], i]

            prev_ints[num] = i

        return [-1, -1]
