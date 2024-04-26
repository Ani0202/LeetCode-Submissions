class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        minInd = 0
        maxInd = 0
        for i in range(indexDifference, len(nums)):
            start = i - indexDifference
            if nums[start] < nums[minInd]:
                minInd = start

            if nums[start] > nums[maxInd]:
                maxInd = start

            if nums[i] - nums[minInd] >= valueDifference:
                return [minInd, i]

            if nums[maxInd] - nums[i] >= valueDifference:
                return [maxInd, i]

        return [-1, -1]
