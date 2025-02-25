class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        prevMax = arrays[0][-1]
        prevMin = arrays[0][0]
        ans = -1
        for array in arrays[1:]:
            ans = max(ans, array[-1] - prevMin, prevMax - array[0])
            prevMin = min(prevMin, array[0])
            prevMax = max(prevMax, array[-1])

        return ans
