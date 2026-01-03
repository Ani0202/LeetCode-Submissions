class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        prev_nums = set()
        for num in nums:
            if num in prev_nums:
                return num

            prev_nums.add(num)

        return -1
