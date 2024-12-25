class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = dict()
        for val in magazine:
            hmap[val] = hmap.get(val, 0) + 1

        for val in ransomNote:
            if val not in hmap or hmap[val] == 0:
                return False

            hmap[val] -= 1

        return True
