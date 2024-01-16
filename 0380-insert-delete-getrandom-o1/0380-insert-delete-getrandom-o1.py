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
        lastEle = self.arr[-1]
        indRem = self.hmap[val]
        self.arr[indRem] = lastEle
        self.hmap[lastEle] = indRem
        self.arr.pop()
        del self.hmap[val]
        return True
        

    def getRandom(self) -> int:
        return choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()