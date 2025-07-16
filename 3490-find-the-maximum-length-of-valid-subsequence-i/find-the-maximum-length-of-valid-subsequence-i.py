class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        even = 0
        odd = 0
        altEven = 0
        altOdd = 0
        for i in range(n):
            if nums[i] % 2 == 0:
                even += 1
                altEven = max(altEven, altOdd + 1)
            else:
                odd += 1
                altOdd = max(altOdd, altEven + 1)

        return max(odd, even, altEven, altOdd)
