class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = nums[0]
        count = 1
        for i in nums[1:]:
            if i == ans:
                count += 1
            else:
                count -= 1

            if count == 0:
                ans = i
                count = 1

        return ans