class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 0
        n = len(path)
        stack = []
        while i < n:
            i += 1
            name = ""
            while i < n and path[i] != "/":
                name += path[i]
                i += 1

            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != ".":
                stack.append(name)

        return "/" + "/".join(stack)
