class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = dict()
        for l in s:
            hmap[l] = hmap.get(l, 0) + 1

        for l in t:
            if l not in hmap or hmap[l] == 0:
                return False
            hmap[l] -= 1

        return True
