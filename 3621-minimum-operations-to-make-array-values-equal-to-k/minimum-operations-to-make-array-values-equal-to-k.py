class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        visit = set()
        ans = 0
        for num in nums:
            if num < k:
                return -1

            if num != k and num not in visit:
                ans += 1
                visit.add(num)

        return ans
