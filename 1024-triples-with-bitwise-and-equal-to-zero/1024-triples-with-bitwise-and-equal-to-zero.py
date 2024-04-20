class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        hMap = Counter(x & y for x in nums for y in nums)
        ans = 0
        for i, v in hMap.items():
            for num in nums:
                if num & i == 0:
                    ans += v

        return ans
