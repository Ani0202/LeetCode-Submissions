class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hmap = defaultdict(int)
        for i in arr:
            hmap[i] += 1
        values = set()
        for i in hmap.values():
            if i in values:
                return False
            values.add(i)
        return True
        