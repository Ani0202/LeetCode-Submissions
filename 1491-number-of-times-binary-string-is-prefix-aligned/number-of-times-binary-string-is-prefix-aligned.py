class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        n = len(flips)
        max_index = -1
        ans = 0
        for i in range(n):
            max_index = max(max_index, flips[i])
            if i + 1 == max_index:
                ans += 1

        return ans
