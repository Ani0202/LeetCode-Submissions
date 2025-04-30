class SmallestInfiniteSet:

    def __init__(self):
        self.removedEle = set()

    def popSmallest(self) -> int:
        i = 1
        while i in self.removedEle:
            i += 1

        self.removedEle.add(i)
        return i

    def addBack(self, num: int) -> None:
        if num in self.removedEle:
            self.removedEle.remove(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
