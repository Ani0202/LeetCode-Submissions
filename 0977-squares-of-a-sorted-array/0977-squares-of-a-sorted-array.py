class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[i] >= 0:
                break
        j = i - 1
        ans = []
        while j >= 0 and i < n:
            s1 = nums[j] ** 2
            s2 = nums[i] ** 2
            if s1 < s2:
                ans.append(s1)
                j -= 1
            else:
                ans.append(s2)
                i += 1

        while j >= 0:
            ans.append(nums[j] ** 2)
            j -= 1
        while i < n:
            ans.append(nums[i] ** 2)
            i += 1

        return ans
