class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backTrack(i, tempAns, tempSum):
            if tempSum == target:
                ans.append(tempAns[:])
            elif tempSum < target:
                for j in range(i, len(candidates)):
                    tempAns.append(candidates[j])
                    backTrack(j, tempAns, tempSum + candidates[j])
                    tempAns.pop()

        backTrack(0, [], 0)
        return ans
        