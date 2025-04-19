class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def findLess(val):
            count = 0
            i = 0
            j = n - 1
            while i < j:
                add = nums[i] + nums[j]
                if add < val:
                    count += j - i
                    i += 1
                else:
                    j -= 1

            return count

        return findLess(upper + 1) - findLess(lower)
