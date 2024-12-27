class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.letters = [None] * 26


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for l in word:
            if node.letters[ord(l) - ord("a")] is None:
                node.letters[ord(l) - ord("a")] = TrieNode()
            node = node.letters[ord(l) - ord("a")]

        node.isLeaf = True

    def search(self, word: str) -> bool:
        node = self.root
        for l in word:
            if node.letters[ord(l) - ord("a")] is None:
                return False
            node = node.letters[ord(l) - ord("a")]

        return node.isLeaf is True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for l in prefix:
            if node.letters[ord(l) - ord("a")] is None:
                return False
            node = node.letters[ord(l) - ord("a")]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
