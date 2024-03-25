class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ind = abs(i)
            if nums[ind-1] < 0:
                ans.append(ind)
            else:
                nums[ind-1] = -nums[ind-1]

        return ans