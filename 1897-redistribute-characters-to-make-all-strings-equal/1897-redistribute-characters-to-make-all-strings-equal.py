class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        hmap = defaultdict(int)
        n = len(words)
        for word in words:
            for letter in word:
                hmap[letter] += 1
        for value in hmap.values():
            if value % n:
                return False

        return True
        