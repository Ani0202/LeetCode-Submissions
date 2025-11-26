class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        temp = []
        count = 0
        for i in s:
            if i == "(":
                count += 1
                temp.append(i)
            elif i == ")":
                if count > 0:
                    count -= 1
                    temp.append(i)
            else:
                temp.append(i)

        ans = []
        for i in reversed(temp):
            if i == "(" and count > 0:
                count -= 1
            else:
                ans.append(i)

        return "".join(reversed(ans))
