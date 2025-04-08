class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        hmap = dict()
        for i, num in enumerate(sortedNums):
            if num not in hmap:
                hmap[num] = i

        ans = []
        for num in nums:
            ans.append(hmap[num])

        return ans
