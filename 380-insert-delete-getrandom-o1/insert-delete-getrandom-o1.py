class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.hmap = dict()

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.arr.append(val)
        self.hmap[val] = len(self.arr) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hmap:
            return False
        ind = self.hmap[val]
        endVal = self.arr[-1]
        self.arr[ind] = endVal
        self.arr.pop()
        self.hmap[endVal] = ind
        del self.hmap[val]
        return True

    def getRandom(self) -> int:
        ind = random.randint(0, len(self.arr) - 1)
        return self.arr[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
