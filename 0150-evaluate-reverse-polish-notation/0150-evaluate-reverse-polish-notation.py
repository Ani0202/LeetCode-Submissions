class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1 + n2))
            elif i == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 - n1))
            elif i == "*":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n1 * n2))
            elif i == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            else:
                stack.append(int(i))
        return stack[-1]
