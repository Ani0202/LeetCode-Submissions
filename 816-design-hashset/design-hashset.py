class MyHashSet:

    def __init__(self):
        self.hash = 1000
        self.hashSet = [[] for _ in range(self.hash)]

    def add(self, key: int) -> None:
        hashKey = self.getHashKey(key)
        if key not in self.hashSet[hashKey]:
            self.hashSet[hashKey].append(key)

    def remove(self, key: int) -> None:
        hashKey = self.getHashKey(key)
        if key in self.hashSet[hashKey]:
            self.hashSet[hashKey].remove(key)

    def contains(self, key: int) -> bool:
        hashKey = self.getHashKey(key)
        return key in self.hashSet[hashKey]

    def getHashKey(self, key):
        return key % self.hash


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
