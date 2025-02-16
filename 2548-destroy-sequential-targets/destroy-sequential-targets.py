class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        freq = defaultdict(int)
        val = {}
        for num in nums:
            remainder = num % space
            freq[remainder] += 1
            if remainder not in val or num < val[remainder]:
                val[remainder] = num

        count = max(freq.values())
        return min(val[r] for r in freq if freq[r] == count)
