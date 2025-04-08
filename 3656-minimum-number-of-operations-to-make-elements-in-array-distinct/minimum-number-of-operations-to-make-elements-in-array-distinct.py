class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        maxFirstOcc = -1
        visited = dict()
        for i, num in enumerate(nums):
            if num in visited:
                maxFirstOcc = max(maxFirstOcc, visited[num])
            visited[num] = i

        if maxFirstOcc == -1:
            return 0

        return (maxFirstOcc // 3) + 1
