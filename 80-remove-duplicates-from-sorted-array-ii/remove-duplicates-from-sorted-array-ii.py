class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        curr = None
        count = 0
        for num in nums:
            if num == curr:
                count += 1
            else:
                curr = num
                count = 1

            if count <= 2:
                nums[i] = num
                i += 1

        return i
