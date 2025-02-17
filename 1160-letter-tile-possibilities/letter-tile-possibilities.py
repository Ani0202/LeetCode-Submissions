class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ansSet = set()
        self.findWords(tiles, ansSet, "")
        return len(ansSet)

    def findWords(self, tiles, ansSet, word):
        if len(word) != 0:
            ansSet.add(word)

        for i in range(len(tiles)):
            word += tiles[i]
            self.findWords(tiles[:i] + tiles[i + 1 :], ansSet, word)
            word = word[:-1]
