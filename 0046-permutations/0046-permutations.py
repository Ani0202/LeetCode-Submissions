class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backTrack(arr, tempAns):
            if len(arr) == 0:
                ans.append(tempAns[:])
            else:
                for i in range(len(arr)):
                    tempAns.append(arr[i])
                    backTrack(arr[:i] + arr[i+1:], tempAns)
                    tempAns.pop()

        backTrack(nums, [])
        return ans
        