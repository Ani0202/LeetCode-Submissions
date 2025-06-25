class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.count = defaultdict(list)
        self.maxCurr = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.maxCurr = max(self.maxCurr, self.freq[val])
        self.count[self.freq[val]].append(val)

    def pop(self) -> int:
        maxOcc = self.count[self.maxCurr].pop()
        self.freq[maxOcc] -= 1
        if len(self.count[self.maxCurr]) == 0:
            self.maxCurr -= 1

        return maxOcc


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
