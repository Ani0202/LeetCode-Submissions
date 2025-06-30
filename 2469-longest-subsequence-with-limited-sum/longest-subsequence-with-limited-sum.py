class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        sumArr = nums[:]
        for i in range(1, n):
            sumArr[i] += sumArr[i - 1]

        ans = []
        for query in queries:
            l = 0
            h = n - 1
            while l <= h:
                m = l + (h - l) // 2
                if sumArr[m] <= query:
                    l = m + 1
                else:
                    h = m - 1

            ans.append(l)

        return ans
