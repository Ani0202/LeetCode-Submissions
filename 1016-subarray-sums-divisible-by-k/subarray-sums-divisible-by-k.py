class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        hmap[0] = 1
        total = 0
        ans = 0
        for num in nums:
            total += num
            rem = total % k
            ans += hmap[rem]
            hmap[rem] += 1

        return ans
