class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = {0: 1}
        sum_curr = 0
        ans = 0
        for num in nums:
            sum_curr += num
            ans += sum_map.get(sum_curr - k, 0)
            sum_map[sum_curr] = sum_map.get(sum_curr, 0) + 1

        return ans
