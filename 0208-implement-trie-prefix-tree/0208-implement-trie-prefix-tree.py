class trieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

class Trie:

    def __init__(self):
        self.root = trieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            print(node)
            ind = ord(i) - ord('a')
            if node.children[ind] == None:
                node.children[ind] = trieNode()
            node = node.children[ind]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            ind = ord(i) - ord("a")
            if node.children[ind] == None:
                return False
            node = node.children[ind]
        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            ind = ord(i) - ord("a")
            if node.children[ind] == None:
                return False
            node = node.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)