class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hmap = Counter()

        for i, c in enumerate(order):
            hmap[c] = i

        return "".join(sorted(list(s), key=lambda x: hmap[x]))
