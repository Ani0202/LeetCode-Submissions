class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m != n:
            return False
        hmap = dict()
        for i in range(m):
            if s[i] in hmap:
                if hmap[s[i]] != t[i]:
                    return False
            elif t[i] not in hmap.values():
                hmap[s[i]] = t[i]
            else:
                return False

        return True
        