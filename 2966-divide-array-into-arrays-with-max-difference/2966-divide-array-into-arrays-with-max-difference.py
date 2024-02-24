class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        ele = [nums[0]]
        for i in range(1, len(nums)):
            if len(ele) == 3:
                ans.append(ele)
                ele = [nums[i]]
            elif len(ele) == 0 or nums[i] - ele[0] <= k:
                ele.append(nums[i])
            else:
                return []

        if len(ele):
            ans.append(ele)
        return ans
