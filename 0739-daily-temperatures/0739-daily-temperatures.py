class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [ 0 for _ in range(len(temperatures))]
        for i,v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                ind = stack.pop()
                ans[ind] = i-ind
            stack.append(i)

        return ans
        