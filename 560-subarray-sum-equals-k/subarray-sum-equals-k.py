class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = defaultdict(int)
        sum_map[0] = 1
        sum_curr = 0
        ans = 0
        for num in nums:
            sum_curr += num
            ans += sum_map[sum_curr - k]
            sum_map[sum_curr] += 1

        return ans
