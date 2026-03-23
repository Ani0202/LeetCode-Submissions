class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            sorted_str = "".join(i for i in sorted(s))
            anagrams[sorted_str].append(s)

        return [i for i in anagrams.values()]
