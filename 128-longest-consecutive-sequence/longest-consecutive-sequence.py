class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            if num - 1 not in num_set:
                temp = 0
                while num in num_set:
                    temp += 1
                    num += 1

                ans = max(ans, temp)

        return ans
