class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for word in strs:
            sortedWord = "".join(sorted(word))
            hmap[sortedWord].append(word)

        return hmap.values()
        