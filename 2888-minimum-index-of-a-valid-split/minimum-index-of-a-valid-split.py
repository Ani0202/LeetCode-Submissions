class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        count = 1
        dominant = nums[0]
        for num in nums[1:]:
            if num == dominant:
                count += 1
            else:
                count -= 1

            if count == 0:
                dominant = num
                count = 1

        count = 0
        for num in nums:
            if num == dominant:
                count += 1

        domi1 = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                domi1 += 1

            if domi1 > (i + 1) / 2 and (count - domi1) > (n - i - 1) / 2:
                return i

        return -1
