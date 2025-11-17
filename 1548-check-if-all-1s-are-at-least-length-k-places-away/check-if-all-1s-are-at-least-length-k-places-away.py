class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 1:
                j = i + 1
                while j < n and nums[j] != 1:
                    j += 1

                if j < n and j - i - 1 < k:
                    return False

                i = j

            else:
                i += 1

        return True
