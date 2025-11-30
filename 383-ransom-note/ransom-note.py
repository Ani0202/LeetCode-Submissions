class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = dict()
        for letter in magazine:
            magazine_map[letter] = magazine_map.get(letter, 0) + 1

        for letter in ransomNote:
            if magazine_map.get(letter, 0) == 0:
                return False

            magazine_map[letter] -= 1

        return True
