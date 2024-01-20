class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]
        stack = []
        for i,v in enumerate(arr):
            while stack and arr[stack[-1]] >= v:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)

        ans = sum((i - left[i]) * (right[i] - i) * arr[i] for i in range(n))
        return ans % 1000000007
        