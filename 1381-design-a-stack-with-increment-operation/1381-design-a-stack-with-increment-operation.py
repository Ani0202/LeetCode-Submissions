class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = [0 for _ in range(maxSize)]
        self.inc = [0 for _ in range(maxSize)]
        self.curr = -1

    def push(self, x: int) -> None:
        if self.curr < len(self.stack) - 1:
            self.curr += 1
            self.stack[self.curr] = x

    def pop(self) -> int:
        if self.curr < 0:
            return -1
        ans = self.stack[self.curr] + self.inc[self.curr]
        self.curr -= 1
        if self.curr >= 0:
            self.inc[self.curr] += self.inc[self.curr + 1]
        self.inc[self.curr + 1] = 0
        return ans

    def increment(self, k: int, val: int) -> None:
        k = min(k - 1, self.curr)
        if k >= 0:
            self.inc[k] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
