class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        finalLen = len(num) - k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
      
        ans = ''.join(stack[:finalLen])
        return ans.lstrip('0') or '0'