class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()
        uniVal = nums[len(nums) // 2]
        count = 0
        for num in nums:
            if num % x != uniVal % x:
                return -1

            count += abs(uniVal - num) // x

        return count
