class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = False
        consonant = False
        for letter in word:
            if not letter.isalnum():
                return False

            if letter.isalpha():
                if letter.lower() in {"a", "e", "i", "o", "u"}:
                    vowel = True
                else:
                    consonant = True

        return vowel and consonant
