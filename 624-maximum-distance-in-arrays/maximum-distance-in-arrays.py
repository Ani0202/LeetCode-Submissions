class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min1 = float("inf")
        min2 = float("inf")
        max1 = -float("inf")
        max2 = -float("inf")
        minInd1 = -1
        minInd2 = -1
        maxInd1 = -1
        maxInd2 = -1
        for ind, array in enumerate(arrays):
            minArr = min(array)
            maxArr = max(array)
            if minArr <= min1:
                min2 = min1
                minInd2 = minInd1
                min1 = minArr
                minInd1 = ind
            elif minArr <= min2:
                min2 = minArr
                minInd2 = ind

            if maxArr >= max1:
                max2 = max1
                maxInd2 = maxInd1
                max1 = maxArr
                maxInd1 = ind
            elif maxArr >= max2:
                max2 = maxArr
                maxInd2 = ind

        if maxInd1 != minInd1:
            return max1 - min1
        else:
            return max(max1 - min2, max2 - min1)
