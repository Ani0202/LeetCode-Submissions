class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hmap1 = defaultdict(int)
        hmap2 = defaultdict(int)
        m = len(word1)
        n = len(word2)
        if m != n:
            return False
        for i in range(m):
            hmap1[word1[i]] += 1
            hmap2[word2[i]] += 1
        return sorted(hmap1.keys()) == sorted(hmap2.keys()) and sorted(hmap1.values()) == sorted(hmap2.values())
        