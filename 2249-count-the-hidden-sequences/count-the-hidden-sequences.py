class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        minTotal = 0
        maxTotal = 0
        total = 0
        for diff in differences:
            total += diff
            minTotal = min(minTotal, total)
            maxTotal = max(maxTotal, total)

        lowLimit = lower - minTotal
        maxLimit = upper - maxTotal
        if lowLimit > maxLimit:
            return 0
        else:
            return maxLimit - lowLimit + 1
