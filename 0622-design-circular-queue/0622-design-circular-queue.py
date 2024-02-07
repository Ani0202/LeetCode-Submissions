class MyCircularQueue:
    def __init__(self, k: int):
        self.size = k
        self.queue = [0 for _ in range(k)]
        self.start = -1
        self.end = -1

    def enQueue(self, value: int) -> bool:
        if (self.end + 1) % self.size != self.start:
            self.queue[(self.end + 1) % self.size] = value
            self.end = (self.end + 1) % self.size
            if self.start == -1:
                self.start = 0
            return True
        return False

    def deQueue(self) -> bool:
        if self.end == -1:
            return False
        if self.end == self.start:
            self.end = -1
            self.start = -1
        else:
            self.start = (self.start + 1) % self.size
        return True

    def Front(self) -> int:
        if self.start == -1:
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.end == -1:
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        return self.start == -1

    def isFull(self) -> bool:
        return (self.end + 1) % self.size == self.start


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
