class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odds = [nums[i] for i in range(1, n, 2)]

        evens = [nums[i] for i in range(0, n, 2)]

        odds.sort(reverse=True)
        evens.sort()
        i = 0
        ans = []
        while i < len(evens):
            ans.append(evens[i])
            if i < len(odds):
                ans.append(odds[i])

            i += 1

        return ans
