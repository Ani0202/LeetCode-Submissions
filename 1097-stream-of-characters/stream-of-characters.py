class Trie:
    def __init__(self):
        self.tree = dict()
        self.isLeaf = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.suff = ""
        self.trie = Trie()
        for word in words:
            trie = self.trie
            for letter in word[::-1]:
                if letter not in trie.tree:
                    trie.tree[letter] = Trie()

                trie = trie.tree[letter]

            trie.isLeaf = True

    def query(self, letter: str) -> bool:
        self.suff += letter
        trie = self.trie
        for let in self.suff[::-1]:
            if let not in trie.tree:
                return False

            trie = trie.tree[let]
            if trie.isLeaf:
                return True

        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
