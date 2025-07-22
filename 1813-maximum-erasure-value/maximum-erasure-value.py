class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        subArr = set()
        subArr.add(nums[0])
        currScore = nums[0]
        maxScore = nums[0]
        i = 0
        j = 1
        while j < n:
            if nums[j] in subArr:
                while nums[i] != nums[j]:
                    subArr.remove(nums[i])
                    currScore -= nums[i]
                    i += 1

                subArr.remove(nums[i])
                currScore -= nums[i]
                i += 1

            subArr.add(nums[j])
            currScore += nums[j]
            maxScore = max(maxScore, currScore)
            j += 1

        return maxScore
