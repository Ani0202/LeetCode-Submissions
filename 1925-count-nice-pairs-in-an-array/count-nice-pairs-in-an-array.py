class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        diffSet = defaultdict(int)
        ans = 0
        for num in nums:
            revNum = int(str(num)[::-1])
            diff = num - revNum
            ans += diffSet[diff]
            ans %= mod
            diffSet[diff] += 1

        return ans
