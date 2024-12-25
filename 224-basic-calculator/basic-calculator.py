class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        ans, sign = 0, 1
        i, n = 0, len(s)

        while i < n:
            if s[i].isdigit():
                number = 0
                while i < n and s[i].isdigit():
                    number = number * 10 + int(s[i])
                    i += 1
                ans += sign * number
                i -= 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] == "(":
                stack.append(ans)
                stack.append(sign)
                ans, sign = 0, 1
            elif s[i] == ")":
                ans *= stack.pop()
                ans += stack.pop()
            i += 1

        return ans
