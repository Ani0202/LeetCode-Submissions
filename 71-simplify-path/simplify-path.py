class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for name in path.split("/"):
            if name == ".":
                continue
            elif name == "..":
                if stack:
                    stack.pop()
            elif name:
                stack.append(name)

        return "/" + "/".join(stack)
